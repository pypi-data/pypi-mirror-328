# auto-generated file
import json
from cardinal_sdk.model import DecryptedHealthElement, Patient, User, AccessLevel, SecretIdUseOption, SecretIdUseOptionUseAnySharedWithParent, serialize_patient, serialize_secret_id_use_option, HealthElement, serialize_health_element, EncryptedHealthElement, deserialize_health_element, DocIdentifier, IdWithMandatoryRev, HealthElementShareOptions, SubscriptionEventType, EntitySubscriptionConfiguration
from cardinal_sdk.async_utils import execute_async_method_job
from cardinal_sdk.kotlin_types import symbols
from cardinal_sdk.model.CallResult import create_result_from_json, interpret_kt_error
from ctypes import cast, c_char_p
from typing import List, Optional, Dict
from cardinal_sdk.model.specializations import HexString
from cardinal_sdk.filters.FilterOptions import FilterOptions, SortableFilterOptions
from cardinal_sdk.pagination.PaginatedListIterator import PaginatedListIterator
from cardinal_sdk.subscription.EntitySubscription import EntitySubscription


class HealthElementApi:

	class HealthElementFlavouredEncryptedApi:

		def __init__(self, cardinal_sdk):
			self.cardinal_sdk = cardinal_sdk

		async def share_with_async(self, delegate_id: str, health_element: EncryptedHealthElement, options: Optional[HealthElementShareOptions] = None) -> EncryptedHealthElement:
			def do_decode(raw_result):
				return EncryptedHealthElement._deserialize(raw_result)
			payload = {
				"delegateId": delegate_id,
				"healthElement": health_element.__serialize__(),
				"options": options.__serialize__() if options is not None else None,
			}
			return await execute_async_method_job(
				self.cardinal_sdk._executor,
				True,
				do_decode,
				symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.encrypted.shareWithAsync,
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)

		def share_with_blocking(self, delegate_id: str, health_element: EncryptedHealthElement, options: Optional[HealthElementShareOptions] = None) -> EncryptedHealthElement:
			payload = {
				"delegateId": delegate_id,
				"healthElement": health_element.__serialize__(),
				"options": options.__serialize__() if options is not None else None,
			}
			call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.encrypted.shareWithBlocking(
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)
			result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
			symbols.DisposeString(call_result)
			if result_info.failure is not None:
				raise interpret_kt_error(result_info.failure)
			else:
				return_value = EncryptedHealthElement._deserialize(result_info.success)
				return return_value

		async def share_with_many_async(self, health_element: EncryptedHealthElement, delegates: Dict[str, HealthElementShareOptions]) -> EncryptedHealthElement:
			def do_decode(raw_result):
				return EncryptedHealthElement._deserialize(raw_result)
			payload = {
				"healthElement": health_element.__serialize__(),
				"delegates": {k0: v0.__serialize__() for k0, v0 in delegates.items()},
			}
			return await execute_async_method_job(
				self.cardinal_sdk._executor,
				True,
				do_decode,
				symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.encrypted.shareWithManyAsync,
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)

		def share_with_many_blocking(self, health_element: EncryptedHealthElement, delegates: Dict[str, HealthElementShareOptions]) -> EncryptedHealthElement:
			payload = {
				"healthElement": health_element.__serialize__(),
				"delegates": {k0: v0.__serialize__() for k0, v0 in delegates.items()},
			}
			call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.encrypted.shareWithManyBlocking(
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)
			result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
			symbols.DisposeString(call_result)
			if result_info.failure is not None:
				raise interpret_kt_error(result_info.failure)
			else:
				return_value = EncryptedHealthElement._deserialize(result_info.success)
				return return_value

		async def filter_health_elements_by_async(self, filter: FilterOptions[HealthElement]) -> PaginatedListIterator[EncryptedHealthElement]:
			def do_decode(raw_result):
				return PaginatedListIterator[EncryptedHealthElement](
					producer = raw_result,
					deserializer = lambda x: EncryptedHealthElement._deserialize(x),
					executor = self.cardinal_sdk._executor
				)
			payload = {
				"filter": filter.__serialize__(),
			}
			return await execute_async_method_job(
				self.cardinal_sdk._executor,
				False,
				do_decode,
				symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.encrypted.filterHealthElementsByAsync,
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)

		def filter_health_elements_by_blocking(self, filter: FilterOptions[HealthElement]) -> PaginatedListIterator[EncryptedHealthElement]:
			payload = {
				"filter": filter.__serialize__(),
			}
			call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.encrypted.filterHealthElementsByBlocking(
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)
			error_str_pointer = symbols.kotlin.root.com.icure.cardinal.sdk.py.utils.PyResult.get_failure(call_result)
			if error_str_pointer is not None:
				error_data_str = cast(error_str_pointer, c_char_p).value.decode('utf_8')
				symbols.DisposeString(error_str_pointer)
				symbols.DisposeStablePointer(call_result.pinned)
				raise interpret_kt_error(json.loads(error_data_str))
			else:
				class_pointer = symbols.kotlin.root.com.icure.cardinal.sdk.py.utils.PyResult.get_success(call_result)
				symbols.DisposeStablePointer(call_result.pinned)
				return PaginatedListIterator[EncryptedHealthElement](
					producer = class_pointer,
					deserializer = lambda x: EncryptedHealthElement._deserialize(x),
					executor = self.cardinal_sdk._executor
				)

		async def filter_health_elements_by_sorted_async(self, filter: SortableFilterOptions[HealthElement]) -> PaginatedListIterator[EncryptedHealthElement]:
			def do_decode(raw_result):
				return PaginatedListIterator[EncryptedHealthElement](
					producer = raw_result,
					deserializer = lambda x: EncryptedHealthElement._deserialize(x),
					executor = self.cardinal_sdk._executor
				)
			payload = {
				"filter": filter.__serialize__(),
			}
			return await execute_async_method_job(
				self.cardinal_sdk._executor,
				False,
				do_decode,
				symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.encrypted.filterHealthElementsBySortedAsync,
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)

		def filter_health_elements_by_sorted_blocking(self, filter: SortableFilterOptions[HealthElement]) -> PaginatedListIterator[EncryptedHealthElement]:
			payload = {
				"filter": filter.__serialize__(),
			}
			call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.encrypted.filterHealthElementsBySortedBlocking(
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)
			error_str_pointer = symbols.kotlin.root.com.icure.cardinal.sdk.py.utils.PyResult.get_failure(call_result)
			if error_str_pointer is not None:
				error_data_str = cast(error_str_pointer, c_char_p).value.decode('utf_8')
				symbols.DisposeString(error_str_pointer)
				symbols.DisposeStablePointer(call_result.pinned)
				raise interpret_kt_error(json.loads(error_data_str))
			else:
				class_pointer = symbols.kotlin.root.com.icure.cardinal.sdk.py.utils.PyResult.get_success(call_result)
				symbols.DisposeStablePointer(call_result.pinned)
				return PaginatedListIterator[EncryptedHealthElement](
					producer = class_pointer,
					deserializer = lambda x: EncryptedHealthElement._deserialize(x),
					executor = self.cardinal_sdk._executor
				)

		async def undelete_health_element_by_id_async(self, id: str, rev: str) -> EncryptedHealthElement:
			def do_decode(raw_result):
				return EncryptedHealthElement._deserialize(raw_result)
			payload = {
				"id": id,
				"rev": rev,
			}
			return await execute_async_method_job(
				self.cardinal_sdk._executor,
				True,
				do_decode,
				symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.encrypted.undeleteHealthElementByIdAsync,
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)

		def undelete_health_element_by_id_blocking(self, id: str, rev: str) -> EncryptedHealthElement:
			payload = {
				"id": id,
				"rev": rev,
			}
			call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.encrypted.undeleteHealthElementByIdBlocking(
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)
			result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
			symbols.DisposeString(call_result)
			if result_info.failure is not None:
				raise interpret_kt_error(result_info.failure)
			else:
				return_value = EncryptedHealthElement._deserialize(result_info.success)
				return return_value

		async def undelete_health_element_async(self, health_element: HealthElement) -> EncryptedHealthElement:
			def do_decode(raw_result):
				return EncryptedHealthElement._deserialize(raw_result)
			payload = {
				"healthElement": serialize_health_element(health_element),
			}
			return await execute_async_method_job(
				self.cardinal_sdk._executor,
				True,
				do_decode,
				symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.encrypted.undeleteHealthElementAsync,
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)

		def undelete_health_element_blocking(self, health_element: HealthElement) -> EncryptedHealthElement:
			payload = {
				"healthElement": serialize_health_element(health_element),
			}
			call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.encrypted.undeleteHealthElementBlocking(
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)
			result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
			symbols.DisposeString(call_result)
			if result_info.failure is not None:
				raise interpret_kt_error(result_info.failure)
			else:
				return_value = EncryptedHealthElement._deserialize(result_info.success)
				return return_value

		async def modify_health_element_async(self, entity: EncryptedHealthElement) -> EncryptedHealthElement:
			def do_decode(raw_result):
				return EncryptedHealthElement._deserialize(raw_result)
			payload = {
				"entity": entity.__serialize__(),
			}
			return await execute_async_method_job(
				self.cardinal_sdk._executor,
				True,
				do_decode,
				symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.encrypted.modifyHealthElementAsync,
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)

		def modify_health_element_blocking(self, entity: EncryptedHealthElement) -> EncryptedHealthElement:
			payload = {
				"entity": entity.__serialize__(),
			}
			call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.encrypted.modifyHealthElementBlocking(
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)
			result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
			symbols.DisposeString(call_result)
			if result_info.failure is not None:
				raise interpret_kt_error(result_info.failure)
			else:
				return_value = EncryptedHealthElement._deserialize(result_info.success)
				return return_value

		async def modify_health_elements_async(self, entities: List[EncryptedHealthElement]) -> List[EncryptedHealthElement]:
			def do_decode(raw_result):
				return [EncryptedHealthElement._deserialize(x1) for x1 in raw_result]
			payload = {
				"entities": [x0.__serialize__() for x0 in entities],
			}
			return await execute_async_method_job(
				self.cardinal_sdk._executor,
				True,
				do_decode,
				symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.encrypted.modifyHealthElementsAsync,
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)

		def modify_health_elements_blocking(self, entities: List[EncryptedHealthElement]) -> List[EncryptedHealthElement]:
			payload = {
				"entities": [x0.__serialize__() for x0 in entities],
			}
			call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.encrypted.modifyHealthElementsBlocking(
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)
			result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
			symbols.DisposeString(call_result)
			if result_info.failure is not None:
				raise interpret_kt_error(result_info.failure)
			else:
				return_value = [EncryptedHealthElement._deserialize(x1) for x1 in result_info.success]
				return return_value

		async def get_health_element_async(self, entity_id: str) -> EncryptedHealthElement:
			def do_decode(raw_result):
				return EncryptedHealthElement._deserialize(raw_result)
			payload = {
				"entityId": entity_id,
			}
			return await execute_async_method_job(
				self.cardinal_sdk._executor,
				True,
				do_decode,
				symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.encrypted.getHealthElementAsync,
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)

		def get_health_element_blocking(self, entity_id: str) -> EncryptedHealthElement:
			payload = {
				"entityId": entity_id,
			}
			call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.encrypted.getHealthElementBlocking(
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)
			result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
			symbols.DisposeString(call_result)
			if result_info.failure is not None:
				raise interpret_kt_error(result_info.failure)
			else:
				return_value = EncryptedHealthElement._deserialize(result_info.success)
				return return_value

		async def get_health_elements_async(self, entity_ids: List[str]) -> List[EncryptedHealthElement]:
			def do_decode(raw_result):
				return [EncryptedHealthElement._deserialize(x1) for x1 in raw_result]
			payload = {
				"entityIds": [x0 for x0 in entity_ids],
			}
			return await execute_async_method_job(
				self.cardinal_sdk._executor,
				True,
				do_decode,
				symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.encrypted.getHealthElementsAsync,
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)

		def get_health_elements_blocking(self, entity_ids: List[str]) -> List[EncryptedHealthElement]:
			payload = {
				"entityIds": [x0 for x0 in entity_ids],
			}
			call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.encrypted.getHealthElementsBlocking(
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)
			result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
			symbols.DisposeString(call_result)
			if result_info.failure is not None:
				raise interpret_kt_error(result_info.failure)
			else:
				return_value = [EncryptedHealthElement._deserialize(x1) for x1 in result_info.success]
				return return_value

	class HealthElementFlavouredApi:

		def __init__(self, cardinal_sdk):
			self.cardinal_sdk = cardinal_sdk

		async def share_with_async(self, delegate_id: str, health_element: HealthElement, options: Optional[HealthElementShareOptions] = None) -> HealthElement:
			def do_decode(raw_result):
				return deserialize_health_element(raw_result)
			payload = {
				"delegateId": delegate_id,
				"healthElement": serialize_health_element(health_element),
				"options": options.__serialize__() if options is not None else None,
			}
			return await execute_async_method_job(
				self.cardinal_sdk._executor,
				True,
				do_decode,
				symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.tryAndRecover.shareWithAsync,
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)

		def share_with_blocking(self, delegate_id: str, health_element: HealthElement, options: Optional[HealthElementShareOptions] = None) -> HealthElement:
			payload = {
				"delegateId": delegate_id,
				"healthElement": serialize_health_element(health_element),
				"options": options.__serialize__() if options is not None else None,
			}
			call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.tryAndRecover.shareWithBlocking(
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)
			result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
			symbols.DisposeString(call_result)
			if result_info.failure is not None:
				raise interpret_kt_error(result_info.failure)
			else:
				return_value = deserialize_health_element(result_info.success)
				return return_value

		async def share_with_many_async(self, health_element: HealthElement, delegates: Dict[str, HealthElementShareOptions]) -> HealthElement:
			def do_decode(raw_result):
				return deserialize_health_element(raw_result)
			payload = {
				"healthElement": serialize_health_element(health_element),
				"delegates": {k0: v0.__serialize__() for k0, v0 in delegates.items()},
			}
			return await execute_async_method_job(
				self.cardinal_sdk._executor,
				True,
				do_decode,
				symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.tryAndRecover.shareWithManyAsync,
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)

		def share_with_many_blocking(self, health_element: HealthElement, delegates: Dict[str, HealthElementShareOptions]) -> HealthElement:
			payload = {
				"healthElement": serialize_health_element(health_element),
				"delegates": {k0: v0.__serialize__() for k0, v0 in delegates.items()},
			}
			call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.tryAndRecover.shareWithManyBlocking(
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)
			result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
			symbols.DisposeString(call_result)
			if result_info.failure is not None:
				raise interpret_kt_error(result_info.failure)
			else:
				return_value = deserialize_health_element(result_info.success)
				return return_value

		async def filter_health_elements_by_async(self, filter: FilterOptions[HealthElement]) -> PaginatedListIterator[HealthElement]:
			def do_decode(raw_result):
				return PaginatedListIterator[HealthElement](
					producer = raw_result,
					deserializer = lambda x: deserialize_health_element(x),
					executor = self.cardinal_sdk._executor
				)
			payload = {
				"filter": filter.__serialize__(),
			}
			return await execute_async_method_job(
				self.cardinal_sdk._executor,
				False,
				do_decode,
				symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.tryAndRecover.filterHealthElementsByAsync,
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)

		def filter_health_elements_by_blocking(self, filter: FilterOptions[HealthElement]) -> PaginatedListIterator[HealthElement]:
			payload = {
				"filter": filter.__serialize__(),
			}
			call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.tryAndRecover.filterHealthElementsByBlocking(
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)
			error_str_pointer = symbols.kotlin.root.com.icure.cardinal.sdk.py.utils.PyResult.get_failure(call_result)
			if error_str_pointer is not None:
				error_data_str = cast(error_str_pointer, c_char_p).value.decode('utf_8')
				symbols.DisposeString(error_str_pointer)
				symbols.DisposeStablePointer(call_result.pinned)
				raise interpret_kt_error(json.loads(error_data_str))
			else:
				class_pointer = symbols.kotlin.root.com.icure.cardinal.sdk.py.utils.PyResult.get_success(call_result)
				symbols.DisposeStablePointer(call_result.pinned)
				return PaginatedListIterator[HealthElement](
					producer = class_pointer,
					deserializer = lambda x: deserialize_health_element(x),
					executor = self.cardinal_sdk._executor
				)

		async def filter_health_elements_by_sorted_async(self, filter: SortableFilterOptions[HealthElement]) -> PaginatedListIterator[HealthElement]:
			def do_decode(raw_result):
				return PaginatedListIterator[HealthElement](
					producer = raw_result,
					deserializer = lambda x: deserialize_health_element(x),
					executor = self.cardinal_sdk._executor
				)
			payload = {
				"filter": filter.__serialize__(),
			}
			return await execute_async_method_job(
				self.cardinal_sdk._executor,
				False,
				do_decode,
				symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.tryAndRecover.filterHealthElementsBySortedAsync,
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)

		def filter_health_elements_by_sorted_blocking(self, filter: SortableFilterOptions[HealthElement]) -> PaginatedListIterator[HealthElement]:
			payload = {
				"filter": filter.__serialize__(),
			}
			call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.tryAndRecover.filterHealthElementsBySortedBlocking(
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)
			error_str_pointer = symbols.kotlin.root.com.icure.cardinal.sdk.py.utils.PyResult.get_failure(call_result)
			if error_str_pointer is not None:
				error_data_str = cast(error_str_pointer, c_char_p).value.decode('utf_8')
				symbols.DisposeString(error_str_pointer)
				symbols.DisposeStablePointer(call_result.pinned)
				raise interpret_kt_error(json.loads(error_data_str))
			else:
				class_pointer = symbols.kotlin.root.com.icure.cardinal.sdk.py.utils.PyResult.get_success(call_result)
				symbols.DisposeStablePointer(call_result.pinned)
				return PaginatedListIterator[HealthElement](
					producer = class_pointer,
					deserializer = lambda x: deserialize_health_element(x),
					executor = self.cardinal_sdk._executor
				)

		async def undelete_health_element_by_id_async(self, id: str, rev: str) -> HealthElement:
			def do_decode(raw_result):
				return deserialize_health_element(raw_result)
			payload = {
				"id": id,
				"rev": rev,
			}
			return await execute_async_method_job(
				self.cardinal_sdk._executor,
				True,
				do_decode,
				symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.tryAndRecover.undeleteHealthElementByIdAsync,
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)

		def undelete_health_element_by_id_blocking(self, id: str, rev: str) -> HealthElement:
			payload = {
				"id": id,
				"rev": rev,
			}
			call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.tryAndRecover.undeleteHealthElementByIdBlocking(
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)
			result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
			symbols.DisposeString(call_result)
			if result_info.failure is not None:
				raise interpret_kt_error(result_info.failure)
			else:
				return_value = deserialize_health_element(result_info.success)
				return return_value

		async def undelete_health_element_async(self, health_element: HealthElement) -> HealthElement:
			def do_decode(raw_result):
				return deserialize_health_element(raw_result)
			payload = {
				"healthElement": serialize_health_element(health_element),
			}
			return await execute_async_method_job(
				self.cardinal_sdk._executor,
				True,
				do_decode,
				symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.tryAndRecover.undeleteHealthElementAsync,
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)

		def undelete_health_element_blocking(self, health_element: HealthElement) -> HealthElement:
			payload = {
				"healthElement": serialize_health_element(health_element),
			}
			call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.tryAndRecover.undeleteHealthElementBlocking(
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)
			result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
			symbols.DisposeString(call_result)
			if result_info.failure is not None:
				raise interpret_kt_error(result_info.failure)
			else:
				return_value = deserialize_health_element(result_info.success)
				return return_value

		async def modify_health_element_async(self, entity: HealthElement) -> HealthElement:
			def do_decode(raw_result):
				return deserialize_health_element(raw_result)
			payload = {
				"entity": serialize_health_element(entity),
			}
			return await execute_async_method_job(
				self.cardinal_sdk._executor,
				True,
				do_decode,
				symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.tryAndRecover.modifyHealthElementAsync,
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)

		def modify_health_element_blocking(self, entity: HealthElement) -> HealthElement:
			payload = {
				"entity": serialize_health_element(entity),
			}
			call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.tryAndRecover.modifyHealthElementBlocking(
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)
			result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
			symbols.DisposeString(call_result)
			if result_info.failure is not None:
				raise interpret_kt_error(result_info.failure)
			else:
				return_value = deserialize_health_element(result_info.success)
				return return_value

		async def modify_health_elements_async(self, entities: List[HealthElement]) -> List[HealthElement]:
			def do_decode(raw_result):
				return [deserialize_health_element(x1) for x1 in raw_result]
			payload = {
				"entities": [serialize_health_element(x0) for x0 in entities],
			}
			return await execute_async_method_job(
				self.cardinal_sdk._executor,
				True,
				do_decode,
				symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.tryAndRecover.modifyHealthElementsAsync,
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)

		def modify_health_elements_blocking(self, entities: List[HealthElement]) -> List[HealthElement]:
			payload = {
				"entities": [serialize_health_element(x0) for x0 in entities],
			}
			call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.tryAndRecover.modifyHealthElementsBlocking(
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)
			result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
			symbols.DisposeString(call_result)
			if result_info.failure is not None:
				raise interpret_kt_error(result_info.failure)
			else:
				return_value = [deserialize_health_element(x1) for x1 in result_info.success]
				return return_value

		async def get_health_element_async(self, entity_id: str) -> HealthElement:
			def do_decode(raw_result):
				return deserialize_health_element(raw_result)
			payload = {
				"entityId": entity_id,
			}
			return await execute_async_method_job(
				self.cardinal_sdk._executor,
				True,
				do_decode,
				symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.tryAndRecover.getHealthElementAsync,
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)

		def get_health_element_blocking(self, entity_id: str) -> HealthElement:
			payload = {
				"entityId": entity_id,
			}
			call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.tryAndRecover.getHealthElementBlocking(
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)
			result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
			symbols.DisposeString(call_result)
			if result_info.failure is not None:
				raise interpret_kt_error(result_info.failure)
			else:
				return_value = deserialize_health_element(result_info.success)
				return return_value

		async def get_health_elements_async(self, entity_ids: List[str]) -> List[HealthElement]:
			def do_decode(raw_result):
				return [deserialize_health_element(x1) for x1 in raw_result]
			payload = {
				"entityIds": [x0 for x0 in entity_ids],
			}
			return await execute_async_method_job(
				self.cardinal_sdk._executor,
				True,
				do_decode,
				symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.tryAndRecover.getHealthElementsAsync,
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)

		def get_health_elements_blocking(self, entity_ids: List[str]) -> List[HealthElement]:
			payload = {
				"entityIds": [x0 for x0 in entity_ids],
			}
			call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.tryAndRecover.getHealthElementsBlocking(
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)
			result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
			symbols.DisposeString(call_result)
			if result_info.failure is not None:
				raise interpret_kt_error(result_info.failure)
			else:
				return_value = [deserialize_health_element(x1) for x1 in result_info.success]
				return return_value

	def __init__(self, cardinal_sdk):
		self.cardinal_sdk = cardinal_sdk
		self.encrypted = HealthElementApi.HealthElementFlavouredEncryptedApi(self.cardinal_sdk)
		self.try_and_recover = HealthElementApi.HealthElementFlavouredApi(self.cardinal_sdk)

	async def create_health_element_async(self, entity: DecryptedHealthElement) -> DecryptedHealthElement:
		def do_decode(raw_result):
			return DecryptedHealthElement._deserialize(raw_result)
		payload = {
			"entity": entity.__serialize__(),
		}
		return await execute_async_method_job(
			self.cardinal_sdk._executor,
			True,
			do_decode,
			symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.createHealthElementAsync,
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)

	def create_health_element_blocking(self, entity: DecryptedHealthElement) -> DecryptedHealthElement:
		payload = {
			"entity": entity.__serialize__(),
		}
		call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.createHealthElementBlocking(
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)
		result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
		symbols.DisposeString(call_result)
		if result_info.failure is not None:
			raise interpret_kt_error(result_info.failure)
		else:
			return_value = DecryptedHealthElement._deserialize(result_info.success)
			return return_value

	async def create_health_elements_async(self, entities: List[DecryptedHealthElement]) -> List[DecryptedHealthElement]:
		def do_decode(raw_result):
			return [DecryptedHealthElement._deserialize(x1) for x1 in raw_result]
		payload = {
			"entities": [x0.__serialize__() for x0 in entities],
		}
		return await execute_async_method_job(
			self.cardinal_sdk._executor,
			True,
			do_decode,
			symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.createHealthElementsAsync,
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)

	def create_health_elements_blocking(self, entities: List[DecryptedHealthElement]) -> List[DecryptedHealthElement]:
		payload = {
			"entities": [x0.__serialize__() for x0 in entities],
		}
		call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.createHealthElementsBlocking(
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)
		result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
		symbols.DisposeString(call_result)
		if result_info.failure is not None:
			raise interpret_kt_error(result_info.failure)
		else:
			return_value = [DecryptedHealthElement._deserialize(x1) for x1 in result_info.success]
			return return_value

	async def with_encryption_metadata_async(self, base: Optional[DecryptedHealthElement], patient: Patient, user: Optional[User] = None, delegates: Dict[str, AccessLevel] = {}, secret_id: SecretIdUseOption = SecretIdUseOptionUseAnySharedWithParent()) -> DecryptedHealthElement:
		def do_decode(raw_result):
			return DecryptedHealthElement._deserialize(raw_result)
		payload = {
			"base": base.__serialize__() if base is not None else None,
			"patient": serialize_patient(patient),
			"user": user.__serialize__() if user is not None else None,
			"delegates": {k0: v0.__serialize__() for k0, v0 in delegates.items()},
			"secretId": serialize_secret_id_use_option(secret_id),
		}
		return await execute_async_method_job(
			self.cardinal_sdk._executor,
			True,
			do_decode,
			symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.withEncryptionMetadataAsync,
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)

	def with_encryption_metadata_blocking(self, base: Optional[DecryptedHealthElement], patient: Patient, user: Optional[User] = None, delegates: Dict[str, AccessLevel] = {}, secret_id: SecretIdUseOption = SecretIdUseOptionUseAnySharedWithParent()) -> DecryptedHealthElement:
		payload = {
			"base": base.__serialize__() if base is not None else None,
			"patient": serialize_patient(patient),
			"user": user.__serialize__() if user is not None else None,
			"delegates": {k0: v0.__serialize__() for k0, v0 in delegates.items()},
			"secretId": serialize_secret_id_use_option(secret_id),
		}
		call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.withEncryptionMetadataBlocking(
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)
		result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
		symbols.DisposeString(call_result)
		if result_info.failure is not None:
			raise interpret_kt_error(result_info.failure)
		else:
			return_value = DecryptedHealthElement._deserialize(result_info.success)
			return return_value

	async def get_encryption_keys_of_async(self, health_element: HealthElement) -> List[HexString]:
		def do_decode(raw_result):
			return [x1 for x1 in raw_result]
		payload = {
			"healthElement": serialize_health_element(health_element),
		}
		return await execute_async_method_job(
			self.cardinal_sdk._executor,
			True,
			do_decode,
			symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.getEncryptionKeysOfAsync,
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)

	def get_encryption_keys_of_blocking(self, health_element: HealthElement) -> List[HexString]:
		payload = {
			"healthElement": serialize_health_element(health_element),
		}
		call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.getEncryptionKeysOfBlocking(
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)
		result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
		symbols.DisposeString(call_result)
		if result_info.failure is not None:
			raise interpret_kt_error(result_info.failure)
		else:
			return_value = [x1 for x1 in result_info.success]
			return return_value

	async def has_write_access_async(self, health_element: HealthElement) -> bool:
		def do_decode(raw_result):
			return raw_result
		payload = {
			"healthElement": serialize_health_element(health_element),
		}
		return await execute_async_method_job(
			self.cardinal_sdk._executor,
			True,
			do_decode,
			symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.hasWriteAccessAsync,
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)

	def has_write_access_blocking(self, health_element: HealthElement) -> bool:
		payload = {
			"healthElement": serialize_health_element(health_element),
		}
		call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.hasWriteAccessBlocking(
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)
		result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
		symbols.DisposeString(call_result)
		if result_info.failure is not None:
			raise interpret_kt_error(result_info.failure)
		else:
			return_value = result_info.success
			return return_value

	async def decrypt_patient_id_of_async(self, health_element: HealthElement) -> List[str]:
		def do_decode(raw_result):
			return [x1 for x1 in raw_result]
		payload = {
			"healthElement": serialize_health_element(health_element),
		}
		return await execute_async_method_job(
			self.cardinal_sdk._executor,
			True,
			do_decode,
			symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.decryptPatientIdOfAsync,
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)

	def decrypt_patient_id_of_blocking(self, health_element: HealthElement) -> List[str]:
		payload = {
			"healthElement": serialize_health_element(health_element),
		}
		call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.decryptPatientIdOfBlocking(
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)
		result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
		symbols.DisposeString(call_result)
		if result_info.failure is not None:
			raise interpret_kt_error(result_info.failure)
		else:
			return_value = [x1 for x1 in result_info.success]
			return return_value

	async def create_delegation_de_anonymization_metadata_async(self, entity: HealthElement, delegates: List[str]) -> None:
		def do_decode(raw_result):
			return raw_result
		payload = {
			"entity": serialize_health_element(entity),
			"delegates": [x0 for x0 in delegates],
		}
		return await execute_async_method_job(
			self.cardinal_sdk._executor,
			True,
			do_decode,
			symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.createDelegationDeAnonymizationMetadataAsync,
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)

	def create_delegation_de_anonymization_metadata_blocking(self, entity: HealthElement, delegates: List[str]) -> None:
		payload = {
			"entity": serialize_health_element(entity),
			"delegates": [x0 for x0 in delegates],
		}
		call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.createDelegationDeAnonymizationMetadataBlocking(
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)
		result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
		symbols.DisposeString(call_result)
		if result_info.failure is not None:
			raise interpret_kt_error(result_info.failure)

	async def decrypt_async(self, health_element: EncryptedHealthElement) -> DecryptedHealthElement:
		def do_decode(raw_result):
			return DecryptedHealthElement._deserialize(raw_result)
		payload = {
			"healthElement": health_element.__serialize__(),
		}
		return await execute_async_method_job(
			self.cardinal_sdk._executor,
			True,
			do_decode,
			symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.decryptAsync,
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)

	def decrypt_blocking(self, health_element: EncryptedHealthElement) -> DecryptedHealthElement:
		payload = {
			"healthElement": health_element.__serialize__(),
		}
		call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.decryptBlocking(
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)
		result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
		symbols.DisposeString(call_result)
		if result_info.failure is not None:
			raise interpret_kt_error(result_info.failure)
		else:
			return_value = DecryptedHealthElement._deserialize(result_info.success)
			return return_value

	async def try_decrypt_async(self, health_element: EncryptedHealthElement) -> HealthElement:
		def do_decode(raw_result):
			return deserialize_health_element(raw_result)
		payload = {
			"healthElement": health_element.__serialize__(),
		}
		return await execute_async_method_job(
			self.cardinal_sdk._executor,
			True,
			do_decode,
			symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.tryDecryptAsync,
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)

	def try_decrypt_blocking(self, health_element: EncryptedHealthElement) -> HealthElement:
		payload = {
			"healthElement": health_element.__serialize__(),
		}
		call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.tryDecryptBlocking(
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)
		result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
		symbols.DisposeString(call_result)
		if result_info.failure is not None:
			raise interpret_kt_error(result_info.failure)
		else:
			return_value = deserialize_health_element(result_info.success)
			return return_value

	async def match_health_elements_by_async(self, filter: FilterOptions[HealthElement]) -> List[str]:
		def do_decode(raw_result):
			return [x1 for x1 in raw_result]
		payload = {
			"filter": filter.__serialize__(),
		}
		return await execute_async_method_job(
			self.cardinal_sdk._executor,
			True,
			do_decode,
			symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.matchHealthElementsByAsync,
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)

	def match_health_elements_by_blocking(self, filter: FilterOptions[HealthElement]) -> List[str]:
		payload = {
			"filter": filter.__serialize__(),
		}
		call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.matchHealthElementsByBlocking(
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)
		result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
		symbols.DisposeString(call_result)
		if result_info.failure is not None:
			raise interpret_kt_error(result_info.failure)
		else:
			return_value = [x1 for x1 in result_info.success]
			return return_value

	async def match_health_elements_by_sorted_async(self, filter: SortableFilterOptions[HealthElement]) -> List[str]:
		def do_decode(raw_result):
			return [x1 for x1 in raw_result]
		payload = {
			"filter": filter.__serialize__(),
		}
		return await execute_async_method_job(
			self.cardinal_sdk._executor,
			True,
			do_decode,
			symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.matchHealthElementsBySortedAsync,
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)

	def match_health_elements_by_sorted_blocking(self, filter: SortableFilterOptions[HealthElement]) -> List[str]:
		payload = {
			"filter": filter.__serialize__(),
		}
		call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.matchHealthElementsBySortedBlocking(
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)
		result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
		symbols.DisposeString(call_result)
		if result_info.failure is not None:
			raise interpret_kt_error(result_info.failure)
		else:
			return_value = [x1 for x1 in result_info.success]
			return return_value

	async def delete_health_element_by_id_async(self, entity_id: str, rev: Optional[str]) -> DocIdentifier:
		def do_decode(raw_result):
			return DocIdentifier._deserialize(raw_result)
		payload = {
			"entityId": entity_id,
			"rev": rev,
		}
		return await execute_async_method_job(
			self.cardinal_sdk._executor,
			True,
			do_decode,
			symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.deleteHealthElementByIdAsync,
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)

	def delete_health_element_by_id_blocking(self, entity_id: str, rev: Optional[str]) -> DocIdentifier:
		payload = {
			"entityId": entity_id,
			"rev": rev,
		}
		call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.deleteHealthElementByIdBlocking(
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)
		result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
		symbols.DisposeString(call_result)
		if result_info.failure is not None:
			raise interpret_kt_error(result_info.failure)
		else:
			return_value = DocIdentifier._deserialize(result_info.success)
			return return_value

	async def delete_health_elements_by_ids_async(self, entity_ids: List[IdWithMandatoryRev]) -> List[DocIdentifier]:
		def do_decode(raw_result):
			return [DocIdentifier._deserialize(x1) for x1 in raw_result]
		payload = {
			"entityIds": [x0.__serialize__() for x0 in entity_ids],
		}
		return await execute_async_method_job(
			self.cardinal_sdk._executor,
			True,
			do_decode,
			symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.deleteHealthElementsByIdsAsync,
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)

	def delete_health_elements_by_ids_blocking(self, entity_ids: List[IdWithMandatoryRev]) -> List[DocIdentifier]:
		payload = {
			"entityIds": [x0.__serialize__() for x0 in entity_ids],
		}
		call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.deleteHealthElementsByIdsBlocking(
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)
		result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
		symbols.DisposeString(call_result)
		if result_info.failure is not None:
			raise interpret_kt_error(result_info.failure)
		else:
			return_value = [DocIdentifier._deserialize(x1) for x1 in result_info.success]
			return return_value

	async def purge_health_element_by_id_async(self, id: str, rev: str) -> None:
		def do_decode(raw_result):
			return raw_result
		payload = {
			"id": id,
			"rev": rev,
		}
		return await execute_async_method_job(
			self.cardinal_sdk._executor,
			True,
			do_decode,
			symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.purgeHealthElementByIdAsync,
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)

	def purge_health_element_by_id_blocking(self, id: str, rev: str) -> None:
		payload = {
			"id": id,
			"rev": rev,
		}
		call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.purgeHealthElementByIdBlocking(
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)
		result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
		symbols.DisposeString(call_result)
		if result_info.failure is not None:
			raise interpret_kt_error(result_info.failure)

	async def delete_health_element_async(self, health_element: HealthElement) -> DocIdentifier:
		def do_decode(raw_result):
			return DocIdentifier._deserialize(raw_result)
		payload = {
			"healthElement": serialize_health_element(health_element),
		}
		return await execute_async_method_job(
			self.cardinal_sdk._executor,
			True,
			do_decode,
			symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.deleteHealthElementAsync,
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)

	def delete_health_element_blocking(self, health_element: HealthElement) -> DocIdentifier:
		payload = {
			"healthElement": serialize_health_element(health_element),
		}
		call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.deleteHealthElementBlocking(
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)
		result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
		symbols.DisposeString(call_result)
		if result_info.failure is not None:
			raise interpret_kt_error(result_info.failure)
		else:
			return_value = DocIdentifier._deserialize(result_info.success)
			return return_value

	async def delete_health_elements_async(self, health_elements: List[HealthElement]) -> List[DocIdentifier]:
		def do_decode(raw_result):
			return [DocIdentifier._deserialize(x1) for x1 in raw_result]
		payload = {
			"healthElements": [serialize_health_element(x0) for x0 in health_elements],
		}
		return await execute_async_method_job(
			self.cardinal_sdk._executor,
			True,
			do_decode,
			symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.deleteHealthElementsAsync,
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)

	def delete_health_elements_blocking(self, health_elements: List[HealthElement]) -> List[DocIdentifier]:
		payload = {
			"healthElements": [serialize_health_element(x0) for x0 in health_elements],
		}
		call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.deleteHealthElementsBlocking(
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)
		result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
		symbols.DisposeString(call_result)
		if result_info.failure is not None:
			raise interpret_kt_error(result_info.failure)
		else:
			return_value = [DocIdentifier._deserialize(x1) for x1 in result_info.success]
			return return_value

	async def purge_health_element_async(self, health_element: HealthElement) -> None:
		def do_decode(raw_result):
			return raw_result
		payload = {
			"healthElement": serialize_health_element(health_element),
		}
		return await execute_async_method_job(
			self.cardinal_sdk._executor,
			True,
			do_decode,
			symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.purgeHealthElementAsync,
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)

	def purge_health_element_blocking(self, health_element: HealthElement) -> None:
		payload = {
			"healthElement": serialize_health_element(health_element),
		}
		call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.purgeHealthElementBlocking(
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)
		result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
		symbols.DisposeString(call_result)
		if result_info.failure is not None:
			raise interpret_kt_error(result_info.failure)

	async def share_with_async(self, delegate_id: str, health_element: DecryptedHealthElement, options: Optional[HealthElementShareOptions] = None) -> DecryptedHealthElement:
		def do_decode(raw_result):
			return DecryptedHealthElement._deserialize(raw_result)
		payload = {
			"delegateId": delegate_id,
			"healthElement": health_element.__serialize__(),
			"options": options.__serialize__() if options is not None else None,
		}
		return await execute_async_method_job(
			self.cardinal_sdk._executor,
			True,
			do_decode,
			symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.shareWithAsync,
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)

	def share_with_blocking(self, delegate_id: str, health_element: DecryptedHealthElement, options: Optional[HealthElementShareOptions] = None) -> DecryptedHealthElement:
		payload = {
			"delegateId": delegate_id,
			"healthElement": health_element.__serialize__(),
			"options": options.__serialize__() if options is not None else None,
		}
		call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.shareWithBlocking(
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)
		result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
		symbols.DisposeString(call_result)
		if result_info.failure is not None:
			raise interpret_kt_error(result_info.failure)
		else:
			return_value = DecryptedHealthElement._deserialize(result_info.success)
			return return_value

	async def share_with_many_async(self, health_element: DecryptedHealthElement, delegates: Dict[str, HealthElementShareOptions]) -> DecryptedHealthElement:
		def do_decode(raw_result):
			return DecryptedHealthElement._deserialize(raw_result)
		payload = {
			"healthElement": health_element.__serialize__(),
			"delegates": {k0: v0.__serialize__() for k0, v0 in delegates.items()},
		}
		return await execute_async_method_job(
			self.cardinal_sdk._executor,
			True,
			do_decode,
			symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.shareWithManyAsync,
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)

	def share_with_many_blocking(self, health_element: DecryptedHealthElement, delegates: Dict[str, HealthElementShareOptions]) -> DecryptedHealthElement:
		payload = {
			"healthElement": health_element.__serialize__(),
			"delegates": {k0: v0.__serialize__() for k0, v0 in delegates.items()},
		}
		call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.shareWithManyBlocking(
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)
		result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
		symbols.DisposeString(call_result)
		if result_info.failure is not None:
			raise interpret_kt_error(result_info.failure)
		else:
			return_value = DecryptedHealthElement._deserialize(result_info.success)
			return return_value

	async def filter_health_elements_by_async(self, filter: FilterOptions[HealthElement]) -> PaginatedListIterator[DecryptedHealthElement]:
		def do_decode(raw_result):
			return PaginatedListIterator[DecryptedHealthElement](
				producer = raw_result,
				deserializer = lambda x: DecryptedHealthElement._deserialize(x),
				executor = self.cardinal_sdk._executor
			)
		payload = {
			"filter": filter.__serialize__(),
		}
		return await execute_async_method_job(
			self.cardinal_sdk._executor,
			False,
			do_decode,
			symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.filterHealthElementsByAsync,
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)

	def filter_health_elements_by_blocking(self, filter: FilterOptions[HealthElement]) -> PaginatedListIterator[DecryptedHealthElement]:
		payload = {
			"filter": filter.__serialize__(),
		}
		call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.filterHealthElementsByBlocking(
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)
		error_str_pointer = symbols.kotlin.root.com.icure.cardinal.sdk.py.utils.PyResult.get_failure(call_result)
		if error_str_pointer is not None:
			error_data_str = cast(error_str_pointer, c_char_p).value.decode('utf_8')
			symbols.DisposeString(error_str_pointer)
			symbols.DisposeStablePointer(call_result.pinned)
			raise interpret_kt_error(json.loads(error_data_str))
		else:
			class_pointer = symbols.kotlin.root.com.icure.cardinal.sdk.py.utils.PyResult.get_success(call_result)
			symbols.DisposeStablePointer(call_result.pinned)
			return PaginatedListIterator[DecryptedHealthElement](
				producer = class_pointer,
				deserializer = lambda x: DecryptedHealthElement._deserialize(x),
				executor = self.cardinal_sdk._executor
			)

	async def filter_health_elements_by_sorted_async(self, filter: SortableFilterOptions[HealthElement]) -> PaginatedListIterator[DecryptedHealthElement]:
		def do_decode(raw_result):
			return PaginatedListIterator[DecryptedHealthElement](
				producer = raw_result,
				deserializer = lambda x: DecryptedHealthElement._deserialize(x),
				executor = self.cardinal_sdk._executor
			)
		payload = {
			"filter": filter.__serialize__(),
		}
		return await execute_async_method_job(
			self.cardinal_sdk._executor,
			False,
			do_decode,
			symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.filterHealthElementsBySortedAsync,
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)

	def filter_health_elements_by_sorted_blocking(self, filter: SortableFilterOptions[HealthElement]) -> PaginatedListIterator[DecryptedHealthElement]:
		payload = {
			"filter": filter.__serialize__(),
		}
		call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.filterHealthElementsBySortedBlocking(
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)
		error_str_pointer = symbols.kotlin.root.com.icure.cardinal.sdk.py.utils.PyResult.get_failure(call_result)
		if error_str_pointer is not None:
			error_data_str = cast(error_str_pointer, c_char_p).value.decode('utf_8')
			symbols.DisposeString(error_str_pointer)
			symbols.DisposeStablePointer(call_result.pinned)
			raise interpret_kt_error(json.loads(error_data_str))
		else:
			class_pointer = symbols.kotlin.root.com.icure.cardinal.sdk.py.utils.PyResult.get_success(call_result)
			symbols.DisposeStablePointer(call_result.pinned)
			return PaginatedListIterator[DecryptedHealthElement](
				producer = class_pointer,
				deserializer = lambda x: DecryptedHealthElement._deserialize(x),
				executor = self.cardinal_sdk._executor
			)

	async def undelete_health_element_by_id_async(self, id: str, rev: str) -> DecryptedHealthElement:
		def do_decode(raw_result):
			return DecryptedHealthElement._deserialize(raw_result)
		payload = {
			"id": id,
			"rev": rev,
		}
		return await execute_async_method_job(
			self.cardinal_sdk._executor,
			True,
			do_decode,
			symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.undeleteHealthElementByIdAsync,
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)

	def undelete_health_element_by_id_blocking(self, id: str, rev: str) -> DecryptedHealthElement:
		payload = {
			"id": id,
			"rev": rev,
		}
		call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.undeleteHealthElementByIdBlocking(
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)
		result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
		symbols.DisposeString(call_result)
		if result_info.failure is not None:
			raise interpret_kt_error(result_info.failure)
		else:
			return_value = DecryptedHealthElement._deserialize(result_info.success)
			return return_value

	async def undelete_health_element_async(self, health_element: HealthElement) -> DecryptedHealthElement:
		def do_decode(raw_result):
			return DecryptedHealthElement._deserialize(raw_result)
		payload = {
			"healthElement": serialize_health_element(health_element),
		}
		return await execute_async_method_job(
			self.cardinal_sdk._executor,
			True,
			do_decode,
			symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.undeleteHealthElementAsync,
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)

	def undelete_health_element_blocking(self, health_element: HealthElement) -> DecryptedHealthElement:
		payload = {
			"healthElement": serialize_health_element(health_element),
		}
		call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.undeleteHealthElementBlocking(
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)
		result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
		symbols.DisposeString(call_result)
		if result_info.failure is not None:
			raise interpret_kt_error(result_info.failure)
		else:
			return_value = DecryptedHealthElement._deserialize(result_info.success)
			return return_value

	async def modify_health_element_async(self, entity: DecryptedHealthElement) -> DecryptedHealthElement:
		def do_decode(raw_result):
			return DecryptedHealthElement._deserialize(raw_result)
		payload = {
			"entity": entity.__serialize__(),
		}
		return await execute_async_method_job(
			self.cardinal_sdk._executor,
			True,
			do_decode,
			symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.modifyHealthElementAsync,
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)

	def modify_health_element_blocking(self, entity: DecryptedHealthElement) -> DecryptedHealthElement:
		payload = {
			"entity": entity.__serialize__(),
		}
		call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.modifyHealthElementBlocking(
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)
		result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
		symbols.DisposeString(call_result)
		if result_info.failure is not None:
			raise interpret_kt_error(result_info.failure)
		else:
			return_value = DecryptedHealthElement._deserialize(result_info.success)
			return return_value

	async def modify_health_elements_async(self, entities: List[DecryptedHealthElement]) -> List[DecryptedHealthElement]:
		def do_decode(raw_result):
			return [DecryptedHealthElement._deserialize(x1) for x1 in raw_result]
		payload = {
			"entities": [x0.__serialize__() for x0 in entities],
		}
		return await execute_async_method_job(
			self.cardinal_sdk._executor,
			True,
			do_decode,
			symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.modifyHealthElementsAsync,
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)

	def modify_health_elements_blocking(self, entities: List[DecryptedHealthElement]) -> List[DecryptedHealthElement]:
		payload = {
			"entities": [x0.__serialize__() for x0 in entities],
		}
		call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.modifyHealthElementsBlocking(
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)
		result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
		symbols.DisposeString(call_result)
		if result_info.failure is not None:
			raise interpret_kt_error(result_info.failure)
		else:
			return_value = [DecryptedHealthElement._deserialize(x1) for x1 in result_info.success]
			return return_value

	async def get_health_element_async(self, entity_id: str) -> DecryptedHealthElement:
		def do_decode(raw_result):
			return DecryptedHealthElement._deserialize(raw_result)
		payload = {
			"entityId": entity_id,
		}
		return await execute_async_method_job(
			self.cardinal_sdk._executor,
			True,
			do_decode,
			symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.getHealthElementAsync,
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)

	def get_health_element_blocking(self, entity_id: str) -> DecryptedHealthElement:
		payload = {
			"entityId": entity_id,
		}
		call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.getHealthElementBlocking(
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)
		result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
		symbols.DisposeString(call_result)
		if result_info.failure is not None:
			raise interpret_kt_error(result_info.failure)
		else:
			return_value = DecryptedHealthElement._deserialize(result_info.success)
			return return_value

	async def get_health_elements_async(self, entity_ids: List[str]) -> List[DecryptedHealthElement]:
		def do_decode(raw_result):
			return [DecryptedHealthElement._deserialize(x1) for x1 in raw_result]
		payload = {
			"entityIds": [x0 for x0 in entity_ids],
		}
		return await execute_async_method_job(
			self.cardinal_sdk._executor,
			True,
			do_decode,
			symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.getHealthElementsAsync,
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)

	def get_health_elements_blocking(self, entity_ids: List[str]) -> List[DecryptedHealthElement]:
		payload = {
			"entityIds": [x0 for x0 in entity_ids],
		}
		call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.getHealthElementsBlocking(
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)
		result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
		symbols.DisposeString(call_result)
		if result_info.failure is not None:
			raise interpret_kt_error(result_info.failure)
		else:
			return_value = [DecryptedHealthElement._deserialize(x1) for x1 in result_info.success]
			return return_value

	async def subscribe_to_events_async(self, events: List[SubscriptionEventType], filter: FilterOptions[HealthElement], subscription_config: Optional[EntitySubscriptionConfiguration] = None) -> EntitySubscription[EncryptedHealthElement]:
		def do_decode(raw_result):
			return EntitySubscription[EncryptedHealthElement](
				producer = raw_result,
				deserializer = lambda x: EncryptedHealthElement._deserialize(x),
				executor = self.cardinal_sdk._executor
			)
		payload = {
			"events": [x0.__serialize__() for x0 in events],
			"filter": filter.__serialize__(),
			"subscriptionConfig": subscription_config.__serialize__() if subscription_config is not None else None,
		}
		return await execute_async_method_job(
			self.cardinal_sdk._executor,
			False,
			do_decode,
			symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.subscribeToEventsAsync,
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)

	def subscribe_to_events_blocking(self, events: List[SubscriptionEventType], filter: FilterOptions[HealthElement], subscription_config: Optional[EntitySubscriptionConfiguration] = None) -> EntitySubscription[EncryptedHealthElement]:
		payload = {
			"events": [x0.__serialize__() for x0 in events],
			"filter": filter.__serialize__(),
			"subscriptionConfig": subscription_config.__serialize__() if subscription_config is not None else None,
		}
		call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.HealthElementApi.subscribeToEventsBlocking(
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)
		error_str_pointer = symbols.kotlin.root.com.icure.cardinal.sdk.py.utils.PyResult.get_failure(call_result)
		if error_str_pointer is not None:
			error_data_str = cast(error_str_pointer, c_char_p).value.decode('utf_8')
			symbols.DisposeString(error_str_pointer)
			symbols.DisposeStablePointer(call_result.pinned)
			raise interpret_kt_error(json.loads(error_data_str))
		else:
			class_pointer = symbols.kotlin.root.com.icure.cardinal.sdk.py.utils.PyResult.get_success(call_result)
			symbols.DisposeStablePointer(call_result.pinned)
			return EntitySubscription[EncryptedHealthElement](
				producer = class_pointer,
				deserializer = lambda x: EncryptedHealthElement._deserialize(x),
				executor = self.cardinal_sdk._executor
			)
