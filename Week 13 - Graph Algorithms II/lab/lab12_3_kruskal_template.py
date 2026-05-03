class PriorityQueueBase:
  class _Item:
    __slots__ = '_key', '_value'

    def __init__(self, k, v):
      self._key = k
      self._value = v

    def __lt__(self, other):
      return self._key < other._key

    def __repr__(self):
      return '({0},{1})'.format(self._key, self._value)

  def is_empty(self):
    return len(self) == 0

  def __len__(self):
    raise NotImplementedError()

  def add(self, key, value):
    raise NotImplementedError()

  def min(self):
    raise NotImplementedError()

  def remove_min(self):
    raise NotImplementedError()

class HeapPriorityQueue(PriorityQueueBase):
  def _parent(self, j):
    return (j-1) // 2

  def _left(self, j):
    return 2*j + 1
  
  def _right(self, j):
    return 2*j + 2

  def _has_left(self, j):
    return self._left(j) < len(self._data)
  
  def _has_right(self, j):
    return self._right(j) < len(self._data)
  
  def _swap(self, i, j):
    self._data[i], self._data[j] = self._data[j], self._data[i]

  def _upheap(self, j):
    parent = self._parent(j)
    if j > 0 and self._data[j] < self._data[parent]:
      self._swap(j, parent)
      self._upheap(parent)
  
  def _downheap(self, j):
    if self._has_left(j):
      left = self._left(j)
      small_child = left
      if self._has_right(j):
        right = self._right(j)
        if self._data[right] < self._data[left]:
          small_child = right
      if self._data[small_child] < self._data[j]:
        self._swap(j, small_child)
        self._downheap(small_child)

  def __init__(self):
    self._data = []

  def __len__(self):
    return len(self._data)

  def add(self, key, value):
    self._data.append(self._Item(key, value))
    self._upheap(len(self._data) - 1)
  
  def min(self):
    if self.is_empty():
      raise ValueError('Priority queue is empty.')
    item = self._data[0]
    return (item._key, item._value)

  def remove_min(self):
    if self.is_empty():
      raise ValueError('Priority queue is empty.')
    self._swap(0, len(self._data) - 1)
    item = self._data.pop()
    self._downheap(0)
    return (item._key, item._value)

class AdaptableHeapPriorityQueue(HeapPriorityQueue):
  class Locator(HeapPriorityQueue._Item):
    __slots__ = '_index'

    def __init__(self, k, v, j):
      super().__init__(k,v)
      self._index = j

  def _swap(self, i, j):
    super()._swap(i,j)
    self._data[i]._index = i
    self._data[j]._index = j

  def _bubble(self, j):
    if j > 0 and self._data[j] < self._data[self._parent(j)]:
      self._upheap(j)
    else:
      self._downheap(j)

  def add(self, key, value):
    token = self.Locator(key, value, len(self._data))
    self._data.append(token)
    self._upheap(len(self._data) - 1)
    return token

  def update(self, loc, newkey, newval):
    j = loc._index
    if not (0 <= j < len(self) and self._data[j] is loc):
      raise ValueError('Invalid locator')
    loc._key = newkey
    loc._value = newval
    self._bubble(j)

  def remove(self, loc):
    j = loc._index
    if not (0 <= j < len(self) and self._data[j] is loc):
      raise ValueError('Invalid locator')
    if j == len(self) - 1:
      self._data.pop()
    else:
      self._swap(j, len(self)-1)
      self._data.pop()
      self._bubble(j)
    return (loc._key, loc._value)

class Graph:
  class Vertex:
    __slots__ = '_element'
  
    def __init__(self, x):
      self._element = x
  
    def element(self):
      return self._element
  
    def __hash__(self):
      return hash(id(self))

    def __str__(self):
      return str(self._element)
    
  class Edge:
    __slots__ = '_origin', '_destination', '_element'
  
    def __init__(self, u, v, x):
      self._origin = u
      self._destination = v
      self._element = x
  
    def endpoints(self):
      return (self._origin, self._destination)
  
    def opposite(self, v):
      if not isinstance(v, Graph.Vertex):
        raise TypeError('v must be a Vertex')
      return self._destination if v is self._origin else self._origin
  
    def element(self):
      return self._element
  
    def __hash__(self):
      return hash( (self._origin, self._destination) )

    def __str__(self):
      return '({0},{1},{2})'.format(self._origin,self._destination,self._element)
    
  def __init__(self, directed=False):
    self._outgoing = {}
    self._incoming = {} if directed else self._outgoing

  def _validate_vertex(self, v):
    if not isinstance(v, self.Vertex):
      raise TypeError('Vertex expected')
    if v not in self._outgoing:
      raise ValueError('Vertex does not belong to this graph.')
    
  def is_directed(self):
    return self._incoming is not self._outgoing

  def vertex_count(self):
    return len(self._outgoing)

  def vertices(self):
    return self._outgoing.keys()

  def edge_count(self):
    total = sum(len(self._outgoing[v]) for v in self._outgoing)
    return total if self.is_directed() else total // 2

  def edges(self):
    result = set()
    for secondary_map in self._outgoing.values():
      result.update(secondary_map.values())
    return result

  def get_edge(self, u, v):
    self._validate_vertex(u)
    self._validate_vertex(v)
    return self._outgoing[u].get(v)

  def degree(self, v, outgoing=True):   
    self._validate_vertex(v)
    adj = self._outgoing if outgoing else self._incoming
    return len(adj[v])

  def incident_edges(self, v, outgoing=True):   
    self._validate_vertex(v)
    adj = self._outgoing if outgoing else self._incoming
    for edge in adj[v].values():
      yield edge

  def insert_vertex(self, x=None):
    v = self.Vertex(x)
    self._outgoing[v] = {}
    if self.is_directed():
      self._incoming[v] = {}
    return v
      
  def insert_edge(self, u, v, x=None):
    if self.get_edge(u, v) is not None:
      raise ValueError('u and v are already adjacent')
    e = self.Edge(u, v, x)
    self._outgoing[u][v] = e
    self._incoming[v][u] = e

  def get_vertex(self, label):
    for v in self.vertices():
      if str(v) == label:
        break
    return v

class Partition:
  class Position:
    __slots__ = '_container', '_element', '_size', '_parent'

    def __init__(self, container, e):
      self._container = container
      self._element = e
      self._size = 1
      self._parent = self

    def element(self):
      return self._element

  def _validate(self, p):
    if not isinstance(p, self.Position):
      raise TypeError('p must be proper Position type')
    if p._container is not self:
      raise ValueError('p does not belong to this container')
    
  def make_group(self, e):
    return self.Position(self, e)

  def find(self, p):
    self._validate(p)
    if p._parent != p:
      p._parent = self.find(p._parent)
    return p._parent
    
  def union(self, p, q):
    a = self.find(p)
    b = self.find(q)
    if a is not b:
      if a._size > b._size:
        b._parent = a
        a._size += b._size
      else:
        a._parent = b
        b._size += a._size

def graph_from_edgelist(E, directed=False):
  g = Graph(directed)
  V = set()
  for e in E:
    V.add(e[0])
    V.add(e[1])

  verts = {}
  for v in V:
    verts[v] = g.insert_vertex(v)

  for e in E:
    src = e[0]
    dest = e[1]
    element = e[2] if len(e) > 2 else None
    g.insert_edge(verts[src],verts[dest],element)

  return g

E4 = (
    ('SFO', 'LAX', 337), ('SFO', 'BOS', 2704), ('SFO', 'ORD', 1846),
    ('SFO', 'DFW', 1464), ('LAX', 'DFW', 1235), ('LAX', 'MIA', 2342),
    ('DFW', 'ORD', 802), ('DFW', 'JFK', 1391), ('DFW', 'MIA', 1121),
    ('ORD', 'BOS', 867), ('ORD', 'PVD', 849), ('ORD', 'JFK', 740),
    ('ORD', 'BWI', 621), ('MIA', 'BWI', 946), ('MIA', 'JFK', 1090),
    ('MIA', 'BOS', 1258), ('BWI', 'JFK', 184), ('JFK', 'PVD', 144),
    ('JFK', 'BOS', 187),
    )

G4 = graph_from_edgelist(E4)

def MST_Kruskal(g):
  tree = []
  pq = HeapPriorityQueue()
  forest = Partition()
  position = {}

  for v in g.vertices():
    position[v] = forest.make_group(v)

  for e in g.edges():
    pq.add(e.element(), e)

  size = g.vertex_count()
  
  while len(tree) != size - 1 and not pq.is_empty():
    weight, edge = pq.remove_min()
    u, v = edge.endpoints()
    a = forest.find(position[u])
    b = forest.find(position[v])

    if a != b:
      tree.append(edge)
      forest.union(a, b)

  return tree

mst_kruskal = MST_Kruskal(G4)
print("Kruskal's MST:")
for edge in mst_kruskal:
  print(edge)