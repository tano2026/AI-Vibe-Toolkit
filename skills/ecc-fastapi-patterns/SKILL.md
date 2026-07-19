---
name: ecc-fastapi-patterns
description: "Vibe Toolkit skill: ecc-fastapi-patterns"
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
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    await engine.dispose()


def create_app() -> FastAPI:
    app = FastAPI(title=settings.app_name, version=settings.app_version, lifespan=lifespan)
    app.add_middleware(CORSMiddleware,
        allow_origins=settings.allowed_origins,
        allow_credentials=settings.allow_credentials,
        allow_methods=settings.allowed_methods,
        allow_headers=settings.allowed_headers)
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
    allowed_origins: list[str] = ["http://localhost:3000"]
    allowed_methods: list[str] = ["GET", "POST", "PATCH", "DELETE", "OPTIONS"]
    allowed_headers: list[str] = ["Authorization", "Content-Type"]
    allow_credentials: bool = True

settings = Settings()
```

---

## Pydantic Schemas (v2)

```python
class UserCreate(BaseModel):
    email: EmailStr
    username: str = Field(min_length=3, max_length=50)
    password: str = Field(min_length=8)
    password_confirm: str

    @model_validator(mode="after")
    def passwords_match(self) -> "UserCreate":
        if self.password != self.password_confirm:
            raise ValueError("Passwords do not match")
        return self

class UserResponse(BaseModel):
    id: int
    is_active: bool
    created_at: datetime
    model_config = {"from_attributes": True}
```

---

## Dependency Injection

```python
from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        try:
            yield session
        except Exception:
            await session.rollback()
            raise

DbDep = Annotated[AsyncSession, Depends(get_db)]
```

---

## Router and Endpoint Design

```python
router = APIRouter()

@router.post("/", response_model=UserResponse, status_code=201)
async def create_user(payload: UserCreate, db: DbDep) -> UserResponse:
    try:
        return await UserService(db).create(payload)
    except DuplicateUserError:
        raise HTTPException(status_code=400, detail="Email already registered")

@router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: int, db: DbDep) -> UserResponse:
    user = await UserService(db).get(user_id)
    if user is None:
        raise HTTPException(status_code=404)
    return user
```

---

## Service Layer

```python
class UserService:
    def __init__(self, db: AsyncSession) -> None:
        self.db = db

    async def create(self, payload: UserCreate) -> User:
        user = User(email=payload.email, username=payload.username,
                    hashed_password=pwd_context.hash(payload.password))
        self.db.add(user)
        try:
            await self.db.commit()
        except IntegrityError as exc:
            await self.db.rollback()
            raise DuplicateUserError from exc
        await self.db.refresh(user)
        return user

    async def list(self, skip: int = 0, limit: int = 20) -> tuple[list[User], int]:
        total = (await self.db.execute(select(func.count(User.id)))).scalar_one()
        result = await self.db.execute(select(User).order_by(User.id).offset(skip).limit(limit))
        return list(result.scalars()), total
```

---

## Testing with httpx and pytest

```python
@pytest_asyncio.fixture
async def client(db_session: AsyncSession):
    app = create_app()
    async def override_get_db():
        yield db_session
    app.dependency_overrides[get_db] = override_get_db
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        yield ac
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

## LLM Chat Bot with Function Calling

Build a premium multi-turn LLM chatbot in FastAPI with structured tool calling, state machine, SSE streaming, provider fallback, and Redis session management.

### Architecture Overview

```
FastAPI Router
  i-- POST /chat               Non-streaming chat endpoint
  i-- POST /chat/stream        SSE streaming endpoint
  i-- GET /chat/history/{session_id}
  i-- GET /agents              Available agent list

Services
  i-- LLMGateway               Provider chain: OpenAI -> Gemini -> Error
  i-- SessionService           Redis + in-memory fallback
  i-- Tool Executors           External API calls (flight search, booking, etc.)

Models (Pydantic)
  i-- ToolCall                 Structured tool I/O
  i-- LLMResponse              Unified response (text | tool_call | error)
  i-- SessionState             Booking state machine
```

### State Machine for Booking Flow

Models a multi-turn flow that collects data across conversation turns:

```python
SESSION_STATES = {
    "idle": {"next": ["search_results"], "suggestions": ["Tìm chuyến bay", "Tr giúp"]},
    "search_results": {"next": ["collecting_passengers"], "suggestions": []},
    "collecting_passengers": {"next": ["awaiting_confirmation"], "suggestions": []},
    "awaiting_confirmation": {"next": ["booking_result"], "suggestions": ["Xc nhn", "Sa", "Hy"]},
    "booking_result": {"next": [], "suggestions": ["Tra cu", "t khc", "H tr"]},
}
```

Route handler checks session step on each request, routes to the correct sub-handler, and transitions state.

### Tool Definitions (OpenAI-Compatible)

Pass these as `tools=TOOLS` to the chat completion API:

```python
TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "search_flight",
            "description": "Search flights by route and date",
            "parameters": {
                "type": "object",
                "properties": {
                    "from": {"type": "string", "description": "Departure airport code (SGN, HAN)"},
                    "to": {"type": "string", "description": "Arrival airport code"},
                    "depart_date": {"type": "string", "description": "Departure date (DD/MM/YYYY)"},
                    "return_date": {"type": "string", "description": "Return date (optional)"},
                    "adults": {"type": "integer", "default": 1},
                    "children": {"type": "integer", "default": 0},
                },
                "required": ["from", "to", "depart_date"],
            },
        }
    },
    {
        "type": "function",
        "function": {
            "name": "book_flight",
            "description": "Book flight after selection and passenger info",
            "parameters": {
                "type": "object",
                "properties": {
                    "flight_id": {"type": "string"},
                    "passengers": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "type": {"type": "string", "enum": ["ADT", "CHD", "INF"]},
                                "firstName": {"type": "string"},
                                "lastName": {"type": "string"},
                            },
                        },
                    },
                },
                "required": ["flight_id", "passengers"],
            },
        }
    },
]
```

### Provider Fallback Chain

Chain multiple providers in priority order. Each falls through on exception:

```python
class LLMGateway:
    """Chain: OpenAI => Gemini => Error."""

    def __init__(self):
        self.openai = AsyncOpenAI(api_key=settings.openai_key)
        self.gemini = genai.GenerativeModel("gemini-2.5-flash")

    async def chat(self, message: str, history: list) -> LLMResponse:
        errors = []
        try:
            return await self._chat_openai(message, history)
        except Exception as e:
            errors.append(f"OpenAI: {e}")
        try:
            return await self._chat_gemini(message, history)
        except Exception as e:
            errors.append(f"Gemini: {e}")
        return LLMResponse(type="error", content="All failed: " + "; ".join(errors))
```

For Gemini, pass tools in `generation_config`:

```python
async def _chat_gemini(self, message: str, history: list) -> LLMResponse:
    gemini_tools = [{"function_declarations": [t["function"] for t in TOOLS]}]
    response = self.gemini.generate_content(
        self._build_gemini_history(history, message),
        generation_config={"temperature": 0.3},
        tools=gemini_tools,
    )
    candidate = response.candidates[0]
    if candidate.content.parts[0].function_call:
        fc = candidate.content.parts[0].function_call
        return LLMResponse(type="tool_call", tool_name=fc.name, tool_args=dict(fc.args))
    return LLMResponse(type="text", content=response.text)
```

### SSE Streaming Endpoint

```python
from fastapi.responses import StreamingResponse
import json

@router.post("/chat/stream")
async def chat_stream(request: StreamRequest):
    async def event_generator():
        try:
            llm = get_llm()
            response = await llm.chat(request.message, history)
            if response.type == "tool_call":
                yield f"data: {json.dumps({'type': 'tool_call', 'tool_name': response.tool_name, 'tool_args': response.tool_args})}\n\n"
            else:
                yield f"data: {json.dumps({'type': 'done', 'content': str(response.content)})}\n\n"
        except Exception as e:
            yield f"data: {json.dumps({'type': 'error', 'content': str(e)})}\n\n"
        finally:
            yield "data: [DONE]\n\n"

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no",
        },
    )
```

### Session Service (Redis + In-Memory Fallback)

```python
import redis.asyncio as redis

class SessionService:
    def __init__(self, redis_url: str | None = None):
        self._redis = None
        if redis_url:
            try:
                self._redis = redis.from_url(redis_url, decode_responses=True)
            except Exception:
                pass
        self._memory: dict[str, dict] = {}

    async def get_messages(self, session_id: str, limit: int = 50) -> list:
        if self._redis:
            raw = await self._redis.lrange(f"chat:{session_id}:msgs", -limit, -1)
            return [ChatMessage.model_validate_json(m) for m in raw]
        return self._memory.get(session_id, {}).get("messages", [])[-limit:]

    async def save_search_results(self, session_id: str, results: dict, formatted: str):
        state = self._memory.setdefault(session_id, {})
        state["search_results"] = results
        state["formatted_results"] = formatted
        if self._redis:
            await self._redis.set(f"chat:{session_id}:state", json.dumps(state), ex=86400)
```

### Dynamic Suggestions

Generate context-aware suggestions based on session state:

```python
def get_suggestions(session_state: dict) -> list[str]:
    step = session_state.get("step", "idle")
    base = SESSION_STATES.get(step, {}).get("suggestions", [])

    if step == "search_results":
        results = session_state.get("search_results", [])
        flight_suggestions = [f"Chn chuyn {i+1}" for i in range(min(3, len(results)))]
        return flight_suggestions + ["Tm li", "Hy"]

    if step == "awaiting_confirmation":
        return ["Xc nhn t", "Sa thng tin", "Hy"]

    return base
```

### Best Practices for LLM Chat Bots

- Use one unified LLMResponse model (text | tool_call | error) to keep frontend contract simple
- Cap conversation history at ~50 messages to control token usage
- Make suggestions context-aware (different per state), not static buttons
- Separate tool definitions from tool execution -- LLM sees definitions, service layer executes
- Add X-Accel-Buffering: no on SSE endpoints to prevent nginx buffering
- Implement graceful degradation: provider fails -> fall through, do not crash
- Use Pydantic model_validator for per-passenger-type field validation
- Test provider chain by intentionally failing the primary provider in dev
- For cost optimization, route through 9-router or similar OpenAI-compatible gateway

See references/llm-chat-bot-fastapi.md for full session architecture code.

### RAG with ChromaDB for Domain Knowledge

Augment the LLM with a local vector knowledge base (ChromaDB + ONNX embedding) for domain-specific questions (airline policies, visa rules, etc).

#### Architecture

```
User message → LLM.chat()
  ├─ LLM.chat() auto-calls _query_rag(message)  →  ChromaDB  →  top-k docs
  └─ RAG context merged into system_prompt        →  LLM response
```

RAG runs automatically inside LLMGateway.chat() — no endpoint changes needed.

#### Key Pattern: Auto-Enrich vs system_override

```python
# ✅ CORRECT: let LLM gateway handle RAG automatically
llm_response = await llm.chat(message=msg, history=history)
# → Gateway queries RAG, enriches system prompt, calls LLM

# ❌ WRONG: passing system_override skips RAG enrichment
llm_response = await llm.chat(message=msg, history=history, system_override=prompt)
# → RAG is bypassed because system_override is not None
```

When you pass system_override, the enrichment code `if system_override is None:` evaluates to False and RAG is skipped. Only pass system_override when you explicitly want to bypass knowledge retrieval.

#### ChromaDB Setup (FastAPI Lifespan)

```python
from app.services.rag_service import init_rag, close_rag

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_rag()      # Seeds Chroma on first run
    yield
    await close_rag()
```

First run downloads a ~79MB ONNX model (all-MiniLM-L6-v2). Cache it once, subsequent starts are instant.

#### Seed Data Structure

Index domain knowledge as typed documents:

```python
# Each doc has text + metadata for filtering
{
    "text": "Hãng VietJet Air (VJ): Hành lý - Xách tay: 1 kiện 7kg.",
    "metadata": {
        "type": "policy",          # "airport" | "airline" | "policy"
        "airline_code": "VJ",
        "category": "baggage",     # "baggage" | "change_fee" | "cancel"
    }
}
```

Query returns top_k results with metadata + cosine distance.

#### Pitfalls

- **system_override blocks RAG**: see above. Always let the gateway auto-enrich.
- **First run is slow**: ONNX model is 79MB, downloads on first init_rag(). ~2 minutes on typical internet.
- **all-MiniLM-L6-v2 is English-biased**: works for domain terms (airline codes, policy keywords) but not deep Vietnamese semantics. Upgrade to paraphrase-multilingual-MiniLM-L12-v2 for production.
- **No GPU needed**: CPU ONNX runtime is ~50ms for <100 docs. For 10K+ docs use Qdrant or remote Chroma.
- **Data persists to .chroma/**: wipe to re-seed. For multi-process deployments use remote vector DB.
- **Don't block startup**: catch init_rag() errors and serve without RAG (health checks must still work).

See references/rag-knowledge-base.md for the full RagService implementation, embedding wrapper, and integration code.

## Best Practices

- Always declare a typed response_model to prevent accidental PII/data leaks.
- Consolidate standard middleware dependency injections via type-aliasing: DbDep = Annotated[...Depends(get_db)].
- Wrap database mutation boundaries gracefully within transactions.
- Parse JWT parameters defensively, expecting potential string/integer cast mismatches.
- Enforce deterministic sorting (e.g. .order_by(Model.id)) on paginated endpoints.
- Isolate authorization checks from core authentication dependencies (401 vs 403).
- Use one unified response model for LLM endpoints.
- Cap conversation history at ~50 messages for token control.
- Make suggestions context-aware per conversation state.
- Separate tool definitions from tool execution.
- Add X-Accel-Buffering: no on SSE endpoints.
- Implement graceful degradation on provider failures.
- Use model_validator for per-passenger-type field validation.