---
name: fastapi-patterns
description: ---
category: development
---

---
name: fastapi-patterns
description: FastAPI best practices covering project structure, Pydantic v2 schemas, dependency injection, async handlers, authentication, authorization, transactional service layers, and testing with httpx and pytest.
origin: ECC
---

# FastAPI Patterns

Modern, production-grade FastAPI development: project layout, Pydantic v2 schemas, dependency injection, async patterns, auth, transactional service methods, and testing.

## Project Structure

```text
my_app/
|-- app/
|   |-- main.py               # App factory, lifespan, middleware
|   |-- config.py             # Settings via pydantic-settings
|   |-- dependencies.py       # Shared FastAPI dependencies
|   |-- database.py           # SQLAlchemy engine + session
|   |-- routers/
|   |   `-- users.py
|   |-- models/               # SQLAlchemy ORM models
|   |   `-- user.py
|   |-- schemas/              # Pydantic request/response schemas
|   |   `-- user.py
|   `-- services/             # Business logic layer
|       `-- user_service.py
|-- tests/
|   |-- conftest.py
|   `-- test_users.py
|-- pyproject.toml
`-- .env
```

---

## App Factory and Lifespan

```python
# app/main.py
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.database import engine, Base
from app.routers import users


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Automatically create tables on startup for ease of use in dev/demo environments.
    # For strict production applications, manage schemas via Alembic migrations instead.
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    # Shutdown: close pooled resources.
    await engine.dispose()


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.app_name,
        version=settings.app_version,
        lifespan=lifespan,
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.allowed_origins,
        allow_credentials=settings.allow_credentials,
        allow_methods=settings.allowed_methods,
        allow_headers=settings.allowed_headers,
    )

    app.include_router(users.router, prefix="/users", tags=["users"])

    return app


app = create_app()
```

---

## Configuration with pydantic-settings

```python
# app/config.py
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    app_name: str = "My App"
    app_version: str = "0.1.0"
    debug: bool = False

    database_url: str
    secret_key: str
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    # Pydantic-settings v2 safely evaluates mutable list literals directly
    allowed_origins: list[str] = ["http://localhost:3000"]
    allowed_methods: list[str] = ["GET", "POST", "PATCH", "DELETE", "OPTIONS"]
    allowed_headers: list[str] = ["Authorization", "Content-Type"]
    allow_credentials: bool = True


settings = Settings()
```

---

## Pydantic Schemas (v2)

```python
# app/schemas/user.py
from datetime import datetime
from pydantic import BaseModel, EmailStr, Field, model_validator


class UserBase(BaseModel):
    email: EmailStr
    username: str = Field(min_length=3, max_length=50)


class UserCreate(UserBase):
    password: str = Field(min_length=8)
    password_confirm: str

    @model_validator(mode="after")
    def passwords_match(self) -> "UserCreate":
        if self.password != self.password_confirm:
            raise ValueError("Passwords do not match")
        return self


class UserUpdate(BaseModel):
    username: str | None = Field(default=None, min_length=3, max_length=50)
    email: EmailStr | None = None


class UserResponse(UserBase):
    id: int
    is_active: bool
    created_at: datetime

    model_config = {"from_attributes": True}


class UserListResponse(BaseModel):
    total: int
    items: list[UserResponse]
```

---

## Dependency Injection

```python
# app/dependencies.py
from typing import Annotated, AsyncGenerator
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.ext.asyncio import AsyncSession

from app.config import settings
from app.database import AsyncSessionLocal
from app.models.user import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/token")


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        try:
            yield session
        except Exception:
            await session.rollback()
            raise


async def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
    db: Annotated[AsyncSession, Depends(get_db)],
) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])
        subject = payload.get("sub")
        if subject is None:
            raise credentials_exception
        user_id = int(subject)
    except (JWTError, TypeError, ValueError):
        raise credentials_exception

    user = await db.get(User, user_id)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)],
) -> User:
    if not current_user.is_active:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Inactive user")
    return current_user


DbDep = Annotated[AsyncSession, Depends(get_db)]
CurrentUserDep = Annotated[User, Depends(get_current_user)]
ActiveUserDep = Annotated[User, Depends(get_current_active_user)]
```

---

## Router and Endpoint Design

```python
# app/routers/users.py
from typing import Annotated
from fastapi import APIRouter, HTTPException, Query, status
from fastapi.security import OAuth2PasswordRequestForm

from app.dependencies import ActiveUserDep, DbDep
from app.schemas.user import UserCreate, UserResponse, UserUpdate, UserListResponse
from app.services.user_service import DuplicateUserError, UserService

router = APIRouter()


@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(payload: UserCreate, db: DbDep) -> UserResponse:
    service = UserService(db)
    try:
        return await service.create(payload)
    except DuplicateUserError:
        raise HTTPException(status_code=400, detail="Email already registered")


@router.get("/me", response_model=UserResponse)
async def get_me(current_user: ActiveUserDep) -> UserResponse:
    return current_user


@router.get("/", response_model=UserListResponse)
async def list_users(
    db: DbDep,
    current_user: ActiveUserDep,
    skip: Annotated[int, Query(ge=0)] = 0,
    limit: Annotated[int, Query(ge=1, le=100)] = 20,
) -> UserListResponse:
    service = UserService(db)
    users, total = await service.list(skip=skip, limit=limit)
    return UserListResponse(total=total, items=users)


@router.patch("/{user_id}", response_model=UserResponse)
async def update_user(
    user_id: int,
    payload: UserUpdate,
    db: DbDep,
    current_user: ActiveUserDep,
) -> UserResponse:
    if current_user.id != user_id:
        raise HTTPException(status_code=403, detail="Not authorized")
    service = UserService(db)
    try:
        user = await service.update(user_id, payload)
    except DuplicateUserError:
        raise HTTPException(status_code=400, detail="Email already registered")
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.post("/token")
async def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: DbDep,
) -> dict[str, str]:
    service = UserService(db)
    token = await service.authenticate(form_data.username, form_data.password)
    if token is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return {"access_token": token, "token_type": "bearer"}
```

---

## Service Layer

```python
# app/services/user_service.py
from datetime import datetime, timedelta, timezone

from jose import jwt
from passlib.context import CryptContext
from sqlalchemy import func, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from app.config import settings
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class DuplicateUserError(Exception):
    """Raised when a unique user field conflicts with an existing row."""


class UserService:
    def __init__(self, db: AsyncSession) -> None:
        self.db = db

    async def get_by_email(self, email: str) -> User | None:
        result = await self.db.execute(select(User).where(User.email == email))
        return result.scalar_one_or_none()

    async def create(self, payload: UserCreate) -> User:
        user = User(
            email=payload.email,
            username=payload.username,
            hashed_password=pwd_context.hash(payload.password),
        )
        self.db.add(user)
        try:
            # Rely on atomic DB constraints rather than race-prone application-level prechecks
            await self.db.commit()
        except IntegrityError as exc:
            await self.db.rollback()
            raise DuplicateUserError from exc
        await self.db.refresh(user)
        return user

    async def list(self, skip: int = 0, limit: int = 20) -> tuple[list[User], int]:
        total_result = await self.db.execute(select(func.count(User.id)))
        total = total_result.scalar_one()
        # Enforce explicit deterministic ordering to ensure reliable pagination
        result = await self.db.execute(
            select(User).order_by(User.id).offset(skip).limit(limit)
        )
        return list(result.scalars()), total

    async def update(self, user_id: int, payload: UserUpdate) -> User | None:
        user = await self.db.get(User, user_id)
        if user is None:
            return None
        for field, value in payload.model_dump(exclude_unset=True).items():
            setattr(user, field, value)
        try:
            await self.db.commit()
        except IntegrityError as exc:
            await self.db.rollback()
            raise DuplicateUserError from exc
        await self.db.refresh(user)
        return user

    async def authenticate(self, email: str, password: str) -> str | None:
        user = await self.get_by_email(email)
        if user is None or not pwd_context.verify(password, user.hashed_password):
            return None
        expire = datetime.now(timezone.utc) + timedelta(
            minutes=settings.access_token_expire_minutes
        )
        return jwt.encode(
            {"sub": str(user.id), "exp": expire},
            settings.secret_key,
            algorithm=settings.algorithm,
        )
```

> **Note on Database Design:** Application-level unique handling requires an underlying unique database index (e.g., `unique=True` on your SQLAlchemy mapping attributes). Without underlying constraints, application layer error-catching cannot safely prevent concurrent race conditions.

---

## Testing with httpx and pytest

```python
# tests/conftest.py
import pytest_asyncio
from httpx import ASGITransport, AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from app.database import Base
from app.dependencies import get_db
from app.main import create_app

TEST_DATABASE_URL = "sqlite+aiosqlite:///:memory:"

engine = create_async_engine(TEST_DATABASE_URL)
TestingSessionLocal = async_sessionmaker(engine, expire_on_commit=False)


@pytest_asyncio.fixture(autouse=True)
async def setup_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest_asyncio.fixture
async def db_session():
    async with TestingSessionLocal() as session:
        yield session
        await session.rollback()


@pytest_asyncio.fixture
async def client(db_session: AsyncSession):
    app = create_app()

    async def override_get_db():
        yield db_session

    app.dependency_overrides[get_db] = override_get_db

    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as ac:
        yield ac


@pytest_asyncio.fixture
async def registered_user(client: AsyncClient) -> dict:
    resp = await client.post("/users/", json={
        "email": "test@example.com",
        "username": "testuser",
        "password": "securepass1",
        "password_confirm": "securepass1",
    })
    assert resp.status_code == 201
    return resp.json()


@pytest_asyncio.fixture
async def auth_token(client: AsyncClient, registered_user: dict) -> str:
    resp = await client.post("/users/token", data={
        "username": "test@example.com",
        "password": "securepass1",
    })
    assert resp.status_code == 200
    return resp.json()["access_token"]


@pytest_asyncio.fixture
async def auth_client(client: AsyncClient, auth_token: str) -> AsyncClient:
    client.headers.update({"Authorization": f"Bearer {auth_token}"})
    return client
```

---

## Anti-Patterns

```python
# Bad: business logic inside route handlers.
@router.post("/users/")
async def create_user(payload: UserCreate, db: DbDep):
    hashed = bcrypt.hash(payload.password)
    user = User(email=payload.email, hashed_password=hashed)
    db.add(user)
    await db.commit()
    return user

# Good: thin route, transactional service handling.
@router.post("/users/", response_model=UserResponse, status_code=201)
async def create_user(payload: UserCreate, db: DbDep):
    try:
        return await UserService(db).create(payload)
    except DuplicateUserError:
        raise HTTPException(status_code=400, detail="Email already registered")


# Bad: sync DB calls in async routes block the event loop.
@router.get("/items/")
async def list_items(db: Session = Depends(get_db)):
    return db.query(Item).all()

# Good: use async SQLAlchemy executions.
@router.get("/items/")
async def list_items(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Item))
    return result.scalars().all()
```

---

## Pitfalls

### 1. Lỗi `ModuleNotFoundError: No module named 'backend'` khi chạy Python script trực tiếp

**Mô tả:** Khi chạy ứng dụng FastAPI (`main.py`) bằng `python main.py` từ bên trong thư mục `backend`, nếu các module trong cùng thư mục đó được import bằng đường dẫn tuyệt đối (ví dụ: `import backend.config`), Python sẽ báo lỗi `ModuleNotFoundError` vì nó tìm kiếm một gói `backend` bên trong chính thư mục `backend` đó.

**Giải pháp:** Chuyển tất cả các import trong các file module (ví dụ: `ai_agent.py`, `flight_monitor.py`, `main.py`) sang dạng tương đối hoặc không có tiền tố `backend` khi chúng nằm cùng cấp.
*   **Ví dụ:**
    *   `import config as config` (thay vì `import backend.config`)
    *   `from ai_agent import chat_with_agent` (thay vì `from backend.ai_agent import ...`)
    *   `from .telegram_bot import start_telegram_polling` (cho các module cùng cấp)

**Kiểm tra:** Đảm bảo tất cả các file Python trong thư mục `backend` đều sử dụng import tương đối hoặc không có tiền tố `backend` cho các module cùng cấp.

### 2. Lỗi `TypeError: _patch_asyncio.<locals>.run() got an unexpected keyword argument 'loop_factory'`

**Mô tả:** Lỗi này thường xuất hiện trên các phiên bản Python mới hơn (như Python 3.14) khi sử dụng `uvicorn` và `nest_asyncio` cùng lúc, do sự không tương thích trong cách `uvicorn` và `asyncio` quản lý vòng lặp sự kiện. Đặc biệt, việc gọi `nest_asyncio.apply()` có thể gây ra xung đột.

**Giải pháp:** Loại bỏ `nest_asyncio.apply()` khỏi file `main.py`. Nếu cần chạy các tác vụ `async` trong môi trường không phải `async` (như Jupyter notebook), hãy xem xét các giải pháp thay thế cho `nest_asyncio` hoặc cấu hình `uvicorn` không sử dụng lại vòng lặp sự kiện hiện có.

**Kiểm tra:** Đảm bảo dòng `nest_asyncio.apply()` đã được comment hoặc xóa khỏi `main.py`.

### 3. Khởi chạy Uvicorn ở chế độ nền (Windows/Git Bash)

**Mô tả:** Khi chạy `uvicorn` như một server ở chế độ nền trên môi trường Windows (sử dụng Git Bash), lệnh `uvicorn main:app ...` có thể không hiển thị output hoặc bị treo nếu không được cấu hình đúng.

**Giải pháp:** Sử dụng `terminal(background=True, notify_on_complete=True, timeout=...)` để chạy `uvicorn`. Điều này cho phép Hermes quản lý tiến trình nền và thông báo khi hoàn tất.

**Ví dụ:**
```python
print(default_api.terminal(background=True, command="cd \"D:\\AI Store\\Hermes Agent API\\backend\" && uvicorn main:app --host 0.0.0.0 --port 8000 --reload", notify_on_complete=True, timeout=300))
```

**Kiểm tra:**
*   Sử dụng `process(action='poll', session_id=...)` để kiểm tra trạng thái tiến trình.
*   Kiểm tra `netstat -ano | grep <port>` để đảm bảo cổng đang lắng nghe.

### 4. Lỗi `on_event is deprecated, use lifespan event handlers instead.`

**Mô tả:** Đây là một cảnh báo deprecation từ FastAPI, cho biết rằng việc sử dụng `@app.on_event("startup")` sẽ không được hỗ trợ trong các phiên bản FastAPI tương lai.

**Giải pháp:** Chuyển đổi sang sử dụng `lifespan event handlers`.

**Ví dụ:**

```python
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Logic chạy khi startup
    asyncio.create_task(flight_monitor.start_monitoring_loop())
    logger.info("Đã đăng ký background task kiểm tra chỗ trống (Flight Monitor).")
    yield
    # Logic chạy khi shutdown
    logger.info("Application is shutting down.")

app = FastAPI(lifespan=lifespan)
```

**Kiểm tra:** Đảm bảo `app.on_event("startup")` đã được thay thế bằng `lifespan` context manager.


### StaticFiles mount at "/" intercepts API routes

`app.mount("/", StaticFiles(...))` registers at index 0 in Starlette's route list — it intercepts ALL requests to `/api/*` routes, returning 405 Method Not Allowed for non-GET methods or falling through to "file not found" instead of reaching the API handler.

```python
# BAD: StaticFiles mounted before API routes — POST /api/chat returns 405
app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")

@app.post("/api/chat")
async def chat(...): ...  # NEVER REACHED
```

**Solutions:**

**Option A — Mount AFTER all API routes (works for `app.add_route`, not `app.mount`):**
```python
# Insert at the END of routes list (Starlette 0.38+)
from starlette.routing import Mount
app.router.routes.append(Mount("/", app=StaticFiles(directory=static_dir, html=True)))
```

**Option B — Catch-all middleware (most reliable):**
```python
from fastapi.staticfiles import StaticFiles
from starlette.responses import Response
import os

static_dir = "frontend"
static_app = StaticFiles(directory=static_dir, html=True)

@app.middleware("http")
async def serve_static_fallback(request, call_next):
    # Try API first
    try:
        return await call_next(request)
    except HTTPException as exc:
        if exc.status_code != 404:
            raise
    # Fall through to static
    file_path = os.path.join(static_dir, request.url.path.lstrip("/") or "index.html")
    if os.path.isfile(file_path):
        return await static_app.get_response(request)
    return await static_app.get_response(scope={"type": "http", "path": "/index.html", ...})
```

**Option C — Separate subdomain or port for static files** (cleanest for production).

### Restoring a corrupted source file

When multiple incremental patches corrupt a Python file (e.g., broken syntax from bad middlewares left in the middle of FastAPI call args):

1. **Find the last known-good backup**: `ls -la *.bak*`, look at sizes + timestamps.
2. **Restore**: `cp file.py.bak file.py`.
3. **Re-apply patches one by one** from the restored baseline — never patch a file that has been partially modified.
4. **Verify syntax** after each patch: `python -c "import py_compile; py_compile.compile('file.py', doraise=True)"`.
5. **If no clean backup exists**: rewrite the file from a known working copy (check git, or construct from memory of the original structure).
6. **Prevention**: after every N patches that affect the same file, do a fresh `cp main.py main.py.stepN` checkpoint.

## Best Practices

- Always declare a typed `response_model` to prevent accidental PII/data leaks and output clean OpenAPI schemas.
- Consolidate standard middleware dependency injections via type-aliasing: `DbDep = Annotated[AsyncSession, Depends(get_db)]`.
- Wrap database mutation boundaries gracefully within transactions inside your service layer, catching structural database errors directly.
- Parse JWT parameters defensively, expecting potential string/integer cast mismatches from modern payload variations.
- Enforce deterministic sorting (e.g., `.order_by(Model.id)`) on all offset/limit paginated endpoints to avoid data skips.
- Isolate authorization checks from core authentication dependencies to provide precise REST status signals (`401` vs `403`).

