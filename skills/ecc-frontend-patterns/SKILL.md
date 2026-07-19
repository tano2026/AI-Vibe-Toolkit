---
name: ecc-frontend-patterns
description: "Vibe Toolkit skill: ecc-frontend-patterns"
---

---
name: frontend-patterns
description: "Frontend development patterns for React, Next.js, state management, performance optimization, and UI best practices."
origin: ECC
---

# Frontend Development Patterns

Modern frontend patterns for React, Next.js, and performant user interfaces.

## When to Activate

- Building React components (composition, props, rendering)
- Managing state (useState, useReducer, Zustand, Context)
- Implementing data fetching (SWR, React Query, server components)
- Optimizing performance (memoization, virtualization, code splitting)
- Working with forms (validation, controlled inputs, Zod schemas)
- Handling client-side routing and navigation
- Building accessible, responsive UI patterns
- **Consuming SSE streaming from an LLM chat backend + state-driven component rendering**

## Component Patterns

### Composition Over Inheritance

```typescript
// PASS: GOOD: Component composition
interface CardProps {
  children: React.ReactNode
  variant?: 'default' | 'outlined'
}

export function Card({ children, variant = 'default' }: CardProps) {
  return <div className={`card card-${variant}`}>{children}</div>
}

export function CardHeader({ children }: { children: React.ReactNode }) {
  return <div className="card-header">{children}</div>
}

export function CardBody({ children }: { children: React.ReactNode }) {
  return <div className="card-body">{children}</div>
}

// Usage
<Card>
  <CardHeader>Title</CardHeader>
  <CardBody>Content</CardBody>
</Card>
```

### Compound Components

```typescript
interface TabsContextValue {
  activeTab: string
  setActiveTab: (tab: string) => void
}

const TabsContext = createContext<TabsContextValue | undefined>(undefined)

export function Tabs({ children, defaultTab }: {
  children: React.ReactNode
  defaultTab: string
}) {
  const [activeTab, setActiveTab] = useState(defaultTab)

  return (
    <TabsContext.Provider value={{ activeTab, setActiveTab }}>
      {children}
    </TabsContext.Provider>
  )
}

export function TabList({ children }: { children: React.ReactNode }) {
  return <div className="tab-list">{children}</div>
}

export function Tab({ id, children }: { id: string, children: React.ReactNode }) {
  const context = useContext(TabsContext)
  if (!context) throw new Error('Tab must be used within Tabs')

  return (
    <button
      className={context.activeTab === id ? 'active' : ''}
      onClick={() => context.setActiveTab(id)}
    >
      {children}
    </button>
  )
}

// Usage
<Tabs defaultTab="overview">
  <TabList>
    <Tab id="overview">Overview</Tab>
    <Tab id="details">Details</Tab>
  </TabList>
</Tabs>
```

### Render Props Pattern

```typescript
interface DataLoaderProps<T> {
  url: string
  children: (data: T | null, loading: boolean, error: Error | null) => React.ReactNode
}

export function DataLoader<T>({ url, children }: DataLoaderProps<T>) {
  const [data, setData] = useState<T | null>(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<Error | null>(null)

  useEffect(() => {
    fetch(url)
      .then(res => res.json())
      .then(setData)
      .catch(setError)
      .finally(() => setLoading(false))
  }, [url])

  return <>{children(data, loading, error)}</>
}

// Usage
<DataLoader<Market[]> url="/api/markets">
  {(markets, loading, error) => {
    if (loading) return <Spinner />
    if (error) return <Error error={error} />
    return <MarketList markets={markets!} />
  }}
</DataLoader>
```

## Custom Hooks Patterns

### State Management Hook

```typescript
export function useToggle(initialValue = false): [boolean, () => void] {
  const [value, setValue] = useState(initialValue)

  const toggle = useCallback(() => {
    setValue(v => !v)
  }, [])

  return [value, toggle]
}

// Usage
const [isOpen, toggleOpen] = useToggle()
```

### Async Data Fetching Hook

```typescript
interface UseQueryOptions<T> {
  onSuccess?: (data: T) => void
  onError?: (error: Error) => void
  enabled?: boolean
}

export function useQuery<T>(
  key: string,
  fetcher: () => Promise<T>,
  options?: UseQueryOptions<T>
) {
  const [data, setData] = useState<T | null>(null)
  const [error, setError] = useState<Error | null>(null)
  const [loading, setLoading] = useState(false)

  const fetcherRef = useRef(fetcher)
  const optionsRef = useRef(options)
  useEffect(() => {
    fetcherRef.current = fetcher
    optionsRef.current = options
  })

  const refetch = useCallback(async () => {
    setLoading(true)
    setError(null)
    try {
      const result = await fetcherRef.current()
      setData(result)
      optionsRef.current?.onSuccess?.(result)
    } catch (err) {
      const error = err as Error
      setError(error)
      optionsRef.current?.onError?.(error)
    } finally {
      setLoading(false)
    }
  }, [])

  const enabled = options?.enabled !== false
  useEffect(() => {
    if (enabled) refetch()
  }, [key, enabled, refetch])

  return { data, error, loading, refetch }
}

// Usage
const { data: markets, loading, error, refetch } = useQuery(
  'markets',
  () => fetch('/api/markets').then(r => r.json()),
  { onSuccess: data => console.log('Fetched', data.length, 'markets') }
)
```

### Debounce Hook

```typescript
export function useDebounce<T>(value: T, delay: number): T {
  const [debouncedValue, setDebouncedValue] = useState<T>(value)
  useEffect(() => {
    const handler = setTimeout(() => setDebouncedValue(value), delay)
    return () => clearTimeout(handler)
  }, [value, delay])
  return debouncedValue
}
```

## State Management Patterns

### Context + Reducer Pattern

```typescript
interface State { markets: Market[]; selectedMarket: Market | null; loading: boolean }
type Action =
  | { type: 'SET_MARKETS'; payload: Market[] }
  | { type: 'SELECT_MARKET'; payload: Market }
  | { type: 'SET_LOADING'; payload: boolean }

function reducer(state: State, action: Action): State {
  switch (action.type) {
    case 'SET_MARKETS': return { ...state, markets: action.payload }
    case 'SELECT_MARKET': return { ...state, selectedMarket: action.payload }
    case 'SET_LOADING': return { ...state, loading: action.payload }
    default: return state
  }
}

const MarketContext = createContext<{ state: State; dispatch: Dispatch<Action> } | undefined>(undefined)

export function MarketProvider({ children }: { children: React.ReactNode }) {
  const [state, dispatch] = useReducer(reducer, { markets: [], selectedMarket: null, loading: false })
  return <MarketContext.Provider value={{ state, dispatch }}>{children}</MarketContext.Provider>
}

export function useMarkets() {
  const context = useContext(MarketContext)
  if (!context) throw new Error('useMarkets must be used within MarketProvider')
  return context
}
```

## Performance Optimization

### Memoization

```typescript
// Copy before sorting - Array.prototype.sort mutates in place
const sortedMarkets = useMemo(() => [...markets].sort((a, b) => b.volume - a.volume), [markets])
const handleSearch = useCallback((query: string) => setSearchQuery(query), [])
export const MarketCard = React.memo<MarketCardProps>(({ market }) => (
  <div className="market-card"><h3>{market.name}</h3><p>{market.description}</p></div>
))
```

### Code Splitting & Lazy Loading

```typescript
const HeavyChart = lazy(() => import('./HeavyChart'))
export function Dashboard() {
  return <Suspense fallback={<ChartSkeleton />}><HeavyChart data={data} /></Suspense>
}
```

## Form Handling Patterns

### Controlled Form with Validation

```typescript
interface FormData { name: string; description: string; endDate: string }
interface FormErrors { name?: string; description?: string; endDate?: string }

export function CreateMarketForm() {
  const [formData, setFormData] = useState<FormData>({ name: '', description: '', endDate: '' })
  const [errors, setErrors] = useState<FormErrors>({})

  const validate = (): boolean => {
    const newErrors: FormErrors = {}
    if (!formData.name.trim()) newErrors.name = 'Name is required'
    if (!formData.description.trim()) newErrors.description = 'Description is required'
    if (!formData.endDate) newErrors.endDate = 'End date is required'
    setErrors(newErrors)
    return Object.keys(newErrors).length === 0
  }

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    if (!validate()) return
    try { await createMarket(formData) } catch (error) { /* handle */ }
  }

  return (
    <form onSubmit={handleSubmit}>
      <input value={formData.name} onChange={e => setFormData(prev => ({ ...prev, name: e.target.value }))} />
      {errors.name && <span className="error">{errors.name}</span>}
      <button type="submit">Create Market</button>
    </form>
  )
}
```

## Error Boundary Pattern

```typescript
export class ErrorBoundary extends React.Component<{ children: React.ReactNode }, { hasError: boolean; error: Error | null }> {
  state = { hasError: false, error: null }
  static getDerivedStateFromError(error: Error) { return { hasError: true, error } }
  componentDidCatch(error: Error, errorInfo: React.ErrorInfo) { console.error('Error boundary caught:', error, errorInfo) }
  render() {
    if (this.state.hasError) return <div className="error-fallback"><h2>Something went wrong</h2><p>{this.state.error?.message}</p><button onClick={() => this.setState({ hasError: false })}>Try again</button></div>
    return this.props.children
  }
}

// Usage
<ErrorBoundary><App /></ErrorBoundary>
```

## SSE Streaming Chat UI Pattern

Consuming Server-Sent Events for real-time LLM chat with state-driven component rendering.

### Architecture

```
streamChat(agent, message, sessionId, onEvent)
  └── POST /api/chat/stream  (SSE)
       ├── {"type":"text", "content":"Xin chào..."}         → real-time token
       ├── {"type":"tool_call", "tool_name":"search"}       → loading state
       ├── {"type":"done", "content":"...", "step":"search_results", "data":[...]}  → final
       └── {"type":"error", "content":"..."}                 → error display
```

### Key Patterns

**1. SSE consumer function** (api.ts):

```typescript
export interface StreamEvent {
  type: "text" | "tool_call" | "done" | "error"
  content?: string; session_id?: string; step?: string; data?: any; suggestions?: string[]
}

export async function streamChat(
  agent: string, message: string, sessionId: string | undefined,
  onEvent: (event: StreamEvent) => void
): Promise<void> {
  const response = await fetch(`${BACKEND_URL}/api/chat/stream`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ agent, message, session_id: sessionId ?? null }),
  })
  const reader = response.body!.getReader()
  const decoder = new TextDecoder()
  let buffer = ""
  while (true) {
    const { done, value } = await reader.read()
    if (done) break
    buffer += decoder.decode(value, { stream: true })
    const lines = buffer.split("\n")
    buffer = lines.pop() || ""
    for (const line of lines) {
      if (line.startsWith("data: ")) {
        const data = line.slice(6).trim()
        if (data === "[DONE]") return
        onEvent(JSON.parse(data))
      }
    }
  }
}
```

**2. State-driven rendering** — render different components per step:
- `search_results` → `<FlightCardChat>` cards
- `collecting_passengers` → `<PassengerForm>` form
- `awaiting_confirmation` → confirm/cancel buttons

**3. Session ref pattern** to avoid stale closures:
```typescript
const sessionIdRef = useRef(sessionId)
sessionIdRef.current = sessionId
```

**4. Text accumulation** — real-time token display:
```typescript
let accumulatedContent = ""
if (event.type === "text" && event.content) {
  accumulatedContent += event.content
  setMessages(prev => { const u = [...prev]; u[u.length-1] = { ...u[u.length-1], content: accumulatedContent }; return u })
}
```

### Pitfalls
- **Stale closures**: SSE callbacks capture `sessionId` at render time. Use `useRef`.
- **Chunked SSE**: Buffer lines across fetch reads — one chunk can split `\\n`.
- **Data field parity**: Backend must send `data` alongside `content` for cards/forms.
- **Loading state**: Replace dots on first SSE event, not after `done` — prevents flash.

See `references/sse-streaming-chat-ui.md` for full implementation.

**Remember**: Modern frontend patterns enable maintainable, performant user interfaces. Choose patterns that fit your project complexity.