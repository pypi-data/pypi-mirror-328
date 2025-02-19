"""Utilities to improve LLMs capabilities when working with SPARQL and RDF."""

__version__ = "0.0.6"

from .utils import SparqlEndpointInfo
from .validate_sparql import validate_sparql_in_msg, validate_sparql_with_void
from .sparql_examples_loader import SparqlExamplesLoader
from .sparql_void_shapes_loader import SparqlVoidShapesLoader, get_shex_dict_from_void, get_shex_from_void
