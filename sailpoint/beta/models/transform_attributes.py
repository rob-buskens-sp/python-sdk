# coding: utf-8

"""
    Identity Security Cloud Beta API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. These APIs are in beta and are subject to change. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.1.0-beta
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401

from typing import Any, List, Optional
from pydantic import BaseModel, Field, StrictStr, ValidationError, field_validator
from sailpoint.beta.models.account_attribute import AccountAttribute
from sailpoint.beta.models.base64_decode import Base64Decode
from sailpoint.beta.models.base64_encode import Base64Encode
from sailpoint.beta.models.concatenation import Concatenation
from sailpoint.beta.models.conditional import Conditional
from sailpoint.beta.models.date_compare import DateCompare
from sailpoint.beta.models.date_format import DateFormat
from sailpoint.beta.models.date_math import DateMath
from sailpoint.beta.models.decompose_diacritical_marks import DecomposeDiacriticalMarks
from sailpoint.beta.models.e164phone import E164phone
from sailpoint.beta.models.first_valid import FirstValid
from sailpoint.beta.models.identity_attribute1 import IdentityAttribute1
from sailpoint.beta.models.index_of import IndexOf
from sailpoint.beta.models.iso3166 import ISO3166
from sailpoint.beta.models.left_pad import LeftPad
from sailpoint.beta.models.lookup import Lookup
from sailpoint.beta.models.lower import Lower
from sailpoint.beta.models.name_normalizer import NameNormalizer
from sailpoint.beta.models.random_alpha_numeric import RandomAlphaNumeric
from sailpoint.beta.models.random_numeric import RandomNumeric
from sailpoint.beta.models.reference import Reference
from sailpoint.beta.models.replace import Replace
from sailpoint.beta.models.replace_all import ReplaceAll
from sailpoint.beta.models.right_pad import RightPad
from sailpoint.beta.models.rule import Rule
from sailpoint.beta.models.split import Split
from sailpoint.beta.models.static import Static
from sailpoint.beta.models.substring import Substring
from sailpoint.beta.models.trim import Trim
from sailpoint.beta.models.upper import Upper
from sailpoint.beta.models.uuid_generator import UUIDGenerator
from typing import Union, Any, List, TYPE_CHECKING, Optional, Dict
from typing_extensions import Literal
from pydantic import StrictStr, Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

TRANSFORMATTRIBUTES_ONE_OF_SCHEMAS = ["AccountAttribute", "Base64Decode", "Base64Encode", "Concatenation", "Conditional", "DateCompare", "DateFormat", "DateMath", "DecomposeDiacriticalMarks", "E164phone", "FirstValid", "ISO3166", "IdentityAttribute1", "IndexOf", "LeftPad", "Lookup", "Lower", "NameNormalizer", "RandomAlphaNumeric", "RandomNumeric", "Reference", "Replace", "ReplaceAll", "RightPad", "Rule", "Split", "Static", "Substring", "Trim", "UUIDGenerator", "Upper"]

class TransformAttributes(BaseModel):
    """
    Meta-data about the transform. Values in this list are specific to the type of transform to be executed.
    """
    # data type: AccountAttribute
    oneof_schema_1_validator: Optional[AccountAttribute] = None
    # data type: Base64Decode
    oneof_schema_2_validator: Optional[Base64Decode] = None
    # data type: Base64Encode
    oneof_schema_3_validator: Optional[Base64Encode] = None
    # data type: Concatenation
    oneof_schema_4_validator: Optional[Concatenation] = None
    # data type: Conditional
    oneof_schema_5_validator: Optional[Conditional] = None
    # data type: DateCompare
    oneof_schema_6_validator: Optional[DateCompare] = None
    # data type: DateFormat
    oneof_schema_7_validator: Optional[DateFormat] = None
    # data type: DateMath
    oneof_schema_8_validator: Optional[DateMath] = None
    # data type: DecomposeDiacriticalMarks
    oneof_schema_9_validator: Optional[DecomposeDiacriticalMarks] = None
    # data type: E164phone
    oneof_schema_10_validator: Optional[E164phone] = None
    # data type: FirstValid
    oneof_schema_11_validator: Optional[FirstValid] = None
    # data type: Rule
    oneof_schema_12_validator: Optional[Rule] = None
    # data type: IdentityAttribute1
    oneof_schema_13_validator: Optional[IdentityAttribute1] = None
    # data type: IndexOf
    oneof_schema_14_validator: Optional[IndexOf] = None
    # data type: ISO3166
    oneof_schema_15_validator: Optional[ISO3166] = None
    # data type: LeftPad
    oneof_schema_16_validator: Optional[LeftPad] = None
    # data type: Lookup
    oneof_schema_17_validator: Optional[Lookup] = None
    # data type: Lower
    oneof_schema_18_validator: Optional[Lower] = None
    # data type: NameNormalizer
    oneof_schema_19_validator: Optional[NameNormalizer] = None
    # data type: RandomAlphaNumeric
    oneof_schema_20_validator: Optional[RandomAlphaNumeric] = None
    # data type: RandomNumeric
    oneof_schema_21_validator: Optional[RandomNumeric] = None
    # data type: Reference
    oneof_schema_22_validator: Optional[Reference] = None
    # data type: ReplaceAll
    oneof_schema_23_validator: Optional[ReplaceAll] = None
    # data type: Replace
    oneof_schema_24_validator: Optional[Replace] = None
    # data type: RightPad
    oneof_schema_25_validator: Optional[RightPad] = None
    # data type: Split
    oneof_schema_26_validator: Optional[Split] = None
    # data type: Static
    oneof_schema_27_validator: Optional[Static] = None
    # data type: Substring
    oneof_schema_28_validator: Optional[Substring] = None
    # data type: Trim
    oneof_schema_29_validator: Optional[Trim] = None
    # data type: Upper
    oneof_schema_30_validator: Optional[Upper] = None
    # data type: UUIDGenerator
    oneof_schema_31_validator: Optional[UUIDGenerator] = None
    actual_instance: Optional[Union[AccountAttribute, Base64Decode, Base64Encode, Concatenation, Conditional, DateCompare, DateFormat, DateMath, DecomposeDiacriticalMarks, E164phone, FirstValid, ISO3166, IdentityAttribute1, IndexOf, LeftPad, Lookup, Lower, NameNormalizer, RandomAlphaNumeric, RandomNumeric, Reference, Replace, ReplaceAll, RightPad, Rule, Split, Static, Substring, Trim, UUIDGenerator, Upper]] = None
    one_of_schemas: List[str] = Literal["AccountAttribute", "Base64Decode", "Base64Encode", "Concatenation", "Conditional", "DateCompare", "DateFormat", "DateMath", "DecomposeDiacriticalMarks", "E164phone", "FirstValid", "ISO3166", "IdentityAttribute1", "IndexOf", "LeftPad", "Lookup", "Lower", "NameNormalizer", "RandomAlphaNumeric", "RandomNumeric", "Reference", "Replace", "ReplaceAll", "RightPad", "Rule", "Split", "Static", "Substring", "Trim", "UUIDGenerator", "Upper"]

    model_config = {
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        if v is None:
            return v

        instance = TransformAttributes.model_construct()
        error_messages = []
        match = 0
        # validate data type: AccountAttribute
        if not isinstance(v, AccountAttribute):
            error_messages.append(f"Error! Input type `{type(v)}` is not `AccountAttribute`")
        else:
            match += 1
        # validate data type: Base64Decode
        if not isinstance(v, Base64Decode):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Base64Decode`")
        else:
            match += 1
        # validate data type: Base64Encode
        if not isinstance(v, Base64Encode):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Base64Encode`")
        else:
            match += 1
        # validate data type: Concatenation
        if not isinstance(v, Concatenation):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Concatenation`")
        else:
            match += 1
        # validate data type: Conditional
        if not isinstance(v, Conditional):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Conditional`")
        else:
            match += 1
        # validate data type: DateCompare
        if not isinstance(v, DateCompare):
            error_messages.append(f"Error! Input type `{type(v)}` is not `DateCompare`")
        else:
            match += 1
        # validate data type: DateFormat
        if not isinstance(v, DateFormat):
            error_messages.append(f"Error! Input type `{type(v)}` is not `DateFormat`")
        else:
            match += 1
        # validate data type: DateMath
        if not isinstance(v, DateMath):
            error_messages.append(f"Error! Input type `{type(v)}` is not `DateMath`")
        else:
            match += 1
        # validate data type: DecomposeDiacriticalMarks
        if not isinstance(v, DecomposeDiacriticalMarks):
            error_messages.append(f"Error! Input type `{type(v)}` is not `DecomposeDiacriticalMarks`")
        else:
            match += 1
        # validate data type: E164phone
        if not isinstance(v, E164phone):
            error_messages.append(f"Error! Input type `{type(v)}` is not `E164phone`")
        else:
            match += 1
        # validate data type: FirstValid
        if not isinstance(v, FirstValid):
            error_messages.append(f"Error! Input type `{type(v)}` is not `FirstValid`")
        else:
            match += 1
        # validate data type: Rule
        if not isinstance(v, Rule):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Rule`")
        else:
            match += 1
        # validate data type: IdentityAttribute1
        if not isinstance(v, IdentityAttribute1):
            error_messages.append(f"Error! Input type `{type(v)}` is not `IdentityAttribute1`")
        else:
            match += 1
        # validate data type: IndexOf
        if not isinstance(v, IndexOf):
            error_messages.append(f"Error! Input type `{type(v)}` is not `IndexOf`")
        else:
            match += 1
        # validate data type: ISO3166
        if not isinstance(v, ISO3166):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ISO3166`")
        else:
            match += 1
        # validate data type: LeftPad
        if not isinstance(v, LeftPad):
            error_messages.append(f"Error! Input type `{type(v)}` is not `LeftPad`")
        else:
            match += 1
        # validate data type: Lookup
        if not isinstance(v, Lookup):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Lookup`")
        else:
            match += 1
        # validate data type: Lower
        if not isinstance(v, Lower):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Lower`")
        else:
            match += 1
        # validate data type: NameNormalizer
        if not isinstance(v, NameNormalizer):
            error_messages.append(f"Error! Input type `{type(v)}` is not `NameNormalizer`")
        else:
            match += 1
        # validate data type: RandomAlphaNumeric
        if not isinstance(v, RandomAlphaNumeric):
            error_messages.append(f"Error! Input type `{type(v)}` is not `RandomAlphaNumeric`")
        else:
            match += 1
        # validate data type: RandomNumeric
        if not isinstance(v, RandomNumeric):
            error_messages.append(f"Error! Input type `{type(v)}` is not `RandomNumeric`")
        else:
            match += 1
        # validate data type: Reference
        if not isinstance(v, Reference):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Reference`")
        else:
            match += 1
        # validate data type: ReplaceAll
        if not isinstance(v, ReplaceAll):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ReplaceAll`")
        else:
            match += 1
        # validate data type: Replace
        if not isinstance(v, Replace):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Replace`")
        else:
            match += 1
        # validate data type: RightPad
        if not isinstance(v, RightPad):
            error_messages.append(f"Error! Input type `{type(v)}` is not `RightPad`")
        else:
            match += 1
        # validate data type: Split
        if not isinstance(v, Split):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Split`")
        else:
            match += 1
        # validate data type: Static
        if not isinstance(v, Static):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Static`")
        else:
            match += 1
        # validate data type: Substring
        if not isinstance(v, Substring):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Substring`")
        else:
            match += 1
        # validate data type: Trim
        if not isinstance(v, Trim):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Trim`")
        else:
            match += 1
        # validate data type: Upper
        if not isinstance(v, Upper):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Upper`")
        else:
            match += 1
        # validate data type: UUIDGenerator
        if not isinstance(v, UUIDGenerator):
            error_messages.append(f"Error! Input type `{type(v)}` is not `UUIDGenerator`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in TransformAttributes with oneOf schemas: AccountAttribute, Base64Decode, Base64Encode, Concatenation, Conditional, DateCompare, DateFormat, DateMath, DecomposeDiacriticalMarks, E164phone, FirstValid, ISO3166, IdentityAttribute1, IndexOf, LeftPad, Lookup, Lower, NameNormalizer, RandomAlphaNumeric, RandomNumeric, Reference, Replace, ReplaceAll, RightPad, Rule, Split, Static, Substring, Trim, UUIDGenerator, Upper. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in TransformAttributes with oneOf schemas: AccountAttribute, Base64Decode, Base64Encode, Concatenation, Conditional, DateCompare, DateFormat, DateMath, DecomposeDiacriticalMarks, E164phone, FirstValid, ISO3166, IdentityAttribute1, IndexOf, LeftPad, Lookup, Lower, NameNormalizer, RandomAlphaNumeric, RandomNumeric, Reference, Replace, ReplaceAll, RightPad, Rule, Split, Static, Substring, Trim, UUIDGenerator, Upper. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        if json_str is None:
            return instance

        error_messages = []
        match = 0

        # deserialize data into AccountAttribute
        try:
            instance.actual_instance = AccountAttribute.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Base64Decode
        try:
            instance.actual_instance = Base64Decode.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Base64Encode
        try:
            instance.actual_instance = Base64Encode.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Concatenation
        try:
            instance.actual_instance = Concatenation.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Conditional
        try:
            instance.actual_instance = Conditional.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into DateCompare
        try:
            instance.actual_instance = DateCompare.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into DateFormat
        try:
            instance.actual_instance = DateFormat.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into DateMath
        try:
            instance.actual_instance = DateMath.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into DecomposeDiacriticalMarks
        try:
            instance.actual_instance = DecomposeDiacriticalMarks.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into E164phone
        try:
            instance.actual_instance = E164phone.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into FirstValid
        try:
            instance.actual_instance = FirstValid.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Rule
        try:
            instance.actual_instance = Rule.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into IdentityAttribute1
        try:
            instance.actual_instance = IdentityAttribute1.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into IndexOf
        try:
            instance.actual_instance = IndexOf.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ISO3166
        try:
            instance.actual_instance = ISO3166.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into LeftPad
        try:
            instance.actual_instance = LeftPad.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Lookup
        try:
            instance.actual_instance = Lookup.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Lower
        try:
            instance.actual_instance = Lower.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into NameNormalizer
        try:
            instance.actual_instance = NameNormalizer.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into RandomAlphaNumeric
        try:
            instance.actual_instance = RandomAlphaNumeric.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into RandomNumeric
        try:
            instance.actual_instance = RandomNumeric.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Reference
        try:
            instance.actual_instance = Reference.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ReplaceAll
        try:
            instance.actual_instance = ReplaceAll.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Replace
        try:
            instance.actual_instance = Replace.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into RightPad
        try:
            instance.actual_instance = RightPad.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Split
        try:
            instance.actual_instance = Split.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Static
        try:
            instance.actual_instance = Static.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Substring
        try:
            instance.actual_instance = Substring.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Trim
        try:
            instance.actual_instance = Trim.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Upper
        try:
            instance.actual_instance = Upper.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into UUIDGenerator
        try:
            instance.actual_instance = UUIDGenerator.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into TransformAttributes with oneOf schemas: AccountAttribute, Base64Decode, Base64Encode, Concatenation, Conditional, DateCompare, DateFormat, DateMath, DecomposeDiacriticalMarks, E164phone, FirstValid, ISO3166, IdentityAttribute1, IndexOf, LeftPad, Lookup, Lower, NameNormalizer, RandomAlphaNumeric, RandomNumeric, Reference, Replace, ReplaceAll, RightPad, Rule, Split, Static, Substring, Trim, UUIDGenerator, Upper. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into TransformAttributes with oneOf schemas: AccountAttribute, Base64Decode, Base64Encode, Concatenation, Conditional, DateCompare, DateFormat, DateMath, DecomposeDiacriticalMarks, E164phone, FirstValid, ISO3166, IdentityAttribute1, IndexOf, LeftPad, Lookup, Lower, NameNormalizer, RandomAlphaNumeric, RandomNumeric, Reference, Replace, ReplaceAll, RightPad, Rule, Split, Static, Substring, Trim, UUIDGenerator, Upper. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        to_json = getattr(self.actual_instance, "to_json", None)
        if callable(to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Dict:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        to_dict = getattr(self.actual_instance, "to_dict", None)
        if callable(to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


