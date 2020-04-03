# Weisfeiler-Lehman Algorithm

An Implementation of 1-Weisfeiler-Lehman Algorithm using Deep Graph Library.

## Usage

### Prerequisites

`Python 3.7.3` + `pipenv`

### Setup

```
pipenv install Pipfile
```

### Isomorphisim Test

Check if the two given graphs are possibly isomorphic by the 1-Weisfeiler-Lehman algorithm.

```
import networkx as nx
from wlkernel.weithfeiler_lehman import is_possibly_isomorphic

G = nx.path_graph(10)
mapping = {i: j for i, j in zip(
    range(N), np.random.permutation(range(10)))}
H = nx.relabel_nodes(G, mapping)

is_possibly_isomorphic(G, H) # True
```

### Graph Kernel

Calculate the Weisfeiler Lehman graph kernel based on the subtree kernel.

```
import networkx as nx
from wlkernel.weithfeiler_lehman import is_possibly_isomorphic

G = nx.path_graph(10)
H = nx.path_graph(10)

subtree_kernel(G, H)
```

### Test

```
pytest .
```

## Reference

- Shervashidze, Nino, et al. "Weisfeiler-lehman graph kernels." Journal of Machine Learning Research 12.Sep (2011): 2539-2561.
- Wang, Minjie, et al. "Deep graph library: Towards efficient and scalable deep learning on graphs." arXiv preprint arXiv:1909.01315 (2019).
- Aric A. Hagberg, Daniel A. Schult and Pieter J. Swart, “Exploring network structure, dynamics, and function using NetworkX”, in Proceedings of the 7th Python in Science Conference (SciPy2008), Gäel Varoquaux, Travis Vaught, and Jarrod Millman (Eds), (Pasadena, CA USA), pp. 11–15, Aug 2008
