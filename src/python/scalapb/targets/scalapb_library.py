from __future__ import (absolute_import, division, generators, nested_scopes, print_function,
                        unicode_literals, with_statement)

import logging

from pants.backend.jvm.targets.import_jars_mixin import ImportJarsMixin
from pants.backend.jvm.targets.jvm_target import JvmTarget
from pants.base.payload import Payload
from pants.base.payload_field import PrimitiveField


logger = logging.getLogger(__name__)

class ScalaPbLibrary(ImportJarsMixin, JvmTarget):
  """A Java library generated from Protocol Buffer IDL files."""

  def __init__(self, payload=None, mports, **kwargs):
    payload = payload or Payload()
    payload.add_fields({
      'import_specs': PrimitiveField(imports or ())
    })
    super(ScalaPbLibrary, self).__init__(payload=payload, **kwargs)