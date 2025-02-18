import json
from typing import Any

from temporalio.api.common.v1 import Payload
from temporalio.converter import (
    CompositePayloadConverter,
    DataConverter,
    DefaultPayloadConverter,
    JSONPlainPayloadConverter,
)

try:  # noqa: SIM105
    from pydantic.json import pydantic_encoder
except ImportError:
    pass


class PydanticJSONPayloadConverter(JSONPlainPayloadConverter):
    """Pydantic JSON payload converter.

    This extends the :py:class:`JSONPlainPayloadConverter` to override
    :py:meth:`to_payload` using the Pydantic encoder.
    """

    def to_payload(self, value: Any) -> Payload | None:
        """Convert all values with Pydantic encoder or fail.

        Like the base class, we fail if we cannot convert. This payload
        converter is expected to be the last in the chain, so it can fail if
        unable to convert.
        """
        # We let JSON conversion errors be thrown to caller
        return Payload(
            metadata={"encoding": self.encoding.encode()},
            data=json.dumps(value, separators=(",", ":"), sort_keys=True, default=pydantic_encoder).encode(),
        )


class PydanticPayloadConverter(CompositePayloadConverter):
    """Payload converter that replaces Temporal JSON conversion with Pydantic
    JSON conversion.
    """

    def __init__(self) -> None:
        super().__init__(
            *(
                converter if not isinstance(converter, JSONPlainPayloadConverter) else PydanticJSONPayloadConverter()
                for converter in DefaultPayloadConverter.default_encoding_payload_converters
            ),
        )


pydantic_data_converter = DataConverter(payload_converter_class=PydanticPayloadConverter)
