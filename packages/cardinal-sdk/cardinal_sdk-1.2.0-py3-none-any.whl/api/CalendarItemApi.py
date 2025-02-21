# auto-generated file
import json
from cardinal_sdk.model import DecryptedCalendarItem, Patient, User, AccessLevel, SecretIdUseOption, SecretIdUseOptionUseAnySharedWithParent, serialize_patient, serialize_secret_id_use_option, CalendarItem, serialize_calendar_item, EncryptedCalendarItem, deserialize_calendar_item, DocIdentifier, IdWithMandatoryRev, CalendarItemShareOptions, SubscriptionEventType, EntitySubscriptionConfiguration
from cardinal_sdk.async_utils import execute_async_method_job
from cardinal_sdk.kotlin_types import symbols
from cardinal_sdk.model.CallResult import create_result_from_json, interpret_kt_error
from ctypes import cast, c_char_p
from typing import Optional, Dict, List
from cardinal_sdk.model.specializations import HexString
from cardinal_sdk.filters.FilterOptions import FilterOptions, SortableFilterOptions
from cardinal_sdk.pagination.PaginatedListIterator import PaginatedListIterator
from cardinal_sdk.subscription.EntitySubscription import EntitySubscription


class CalendarItemApi:

	class CalendarItemFlavouredEncryptedApi:

		def __init__(self, cardinal_sdk):
			self.cardinal_sdk = cardinal_sdk

		async def share_with_async(self, delegate_id: str, calendar_item: EncryptedCalendarItem, options: Optional[CalendarItemShareOptions] = None) -> EncryptedCalendarItem:
			def do_decode(raw_result):
				return EncryptedCalendarItem._deserialize(raw_result)
			payload = {
				"delegateId": delegate_id,
				"calendarItem": calendar_item.__serialize__(),
				"options": options.__serialize__() if options is not None else None,
			}
			return await execute_async_method_job(
				self.cardinal_sdk._executor,
				True,
				do_decode,
				symbols.kotlin.root.com.icure.cardinal.sdk.py.api.CalendarItemApi.encrypted.shareWithAsync,
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)

		def share_with_blocking(self, delegate_id: str, calendar_item: EncryptedCalendarItem, options: Optional[CalendarItemShareOptions] = None) -> EncryptedCalendarItem:
			payload = {
				"delegateId": delegate_id,
				"calendarItem": calendar_item.__serialize__(),
				"options": options.__serialize__() if options is not None else None,
			}
			call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.CalendarItemApi.encrypted.shareWithBlocking(
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)
			result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
			symbols.DisposeString(call_result)
			if result_info.failure is not None:
				raise interpret_kt_error(result_info.failure)
			else:
				return_value = EncryptedCalendarItem._deserialize(result_info.success)
				return return_value

		async def share_with_many_async(self, calendar_item: EncryptedCalendarItem, delegates: Dict[str, CalendarItemShareOptions]) -> EncryptedCalendarItem:
			def do_decode(raw_result):
				return EncryptedCalendarItem._deserialize(raw_result)
			payload = {
				"calendarItem": calendar_item.__serialize__(),
				"delegates": {k0: v0.__serialize__() for k0, v0 in delegates.items()},
			}
			return await execute_async_method_job(
				self.cardinal_sdk._executor,
				True,
				do_decode,
				symbols.kotlin.root.com.icure.cardinal.sdk.py.api.CalendarItemApi.encrypted.shareWithManyAsync,
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)

		def share_with_many_blocking(self, calendar_item: EncryptedCalendarItem, delegates: Dict[str, CalendarItemShareOptions]) -> EncryptedCalendarItem:
			payload = {
				"calendarItem": calendar_item.__serialize__(),
				"delegates": {k0: v0.__serialize__() for k0, v0 in delegates.items()},
			}
			call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.CalendarItemApi.encrypted.shareWithManyBlocking(
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)
			result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
			symbols.DisposeString(call_result)
			if result_info.failure is not None:
				raise interpret_kt_error(result_info.failure)
			else:
				return_value = EncryptedCalendarItem._deserialize(result_info.success)
				return return_value

		async def link_to_patient_async(self, calendar_item: CalendarItem, patient: Patient, share_link_with_delegates: List[str]) -> EncryptedCalendarItem:
			def do_decode(raw_result):
				return EncryptedCalendarItem._deserialize(raw_result)
			payload = {
				"calendarItem": serialize_calendar_item(calendar_item),
				"patient": serialize_patient(patient),
				"shareLinkWithDelegates": [x0 for x0 in share_link_with_delegates],
			}
			return await execute_async_method_job(
				self.cardinal_sdk._executor,
				True,
				do_decode,
				symbols.kotlin.root.com.icure.cardinal.sdk.py.api.CalendarItemApi.encrypted.linkToPatientAsync,
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)

		def link_to_patient_blocking(self, calendar_item: CalendarItem, patient: Patient, share_link_with_delegates: List[str]) -> EncryptedCalendarItem:
			payload = {
				"calendarItem": serialize_calendar_item(calendar_item),
				"patient": serialize_patient(patient),
				"shareLinkWithDelegates": [x0 for x0 in share_link_with_delegates],
			}
			call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.CalendarItemApi.encrypted.linkToPatientBlocking(
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)
			result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
			symbols.DisposeString(call_result)
			if result_info.failure is not None:
				raise interpret_kt_error(result_info.failure)
			else:
				return_value = EncryptedCalendarItem._deserialize(result_info.success)
				return return_value

		async def filter_calendar_items_by_async(self, filter: FilterOptions[CalendarItem]) -> PaginatedListIterator[EncryptedCalendarItem]:
			def do_decode(raw_result):
				return PaginatedListIterator[EncryptedCalendarItem](
					producer = raw_result,
					deserializer = lambda x: EncryptedCalendarItem._deserialize(x),
					executor = self.cardinal_sdk._executor
				)
			payload = {
				"filter": filter.__serialize__(),
			}
			return await execute_async_method_job(
				self.cardinal_sdk._executor,
				False,
				do_decode,
				symbols.kotlin.root.com.icure.cardinal.sdk.py.api.CalendarItemApi.encrypted.filterCalendarItemsByAsync,
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)

		def filter_calendar_items_by_blocking(self, filter: FilterOptions[CalendarItem]) -> PaginatedListIterator[EncryptedCalendarItem]:
			payload = {
				"filter": filter.__serialize__(),
			}
			call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.CalendarItemApi.encrypted.filterCalendarItemsByBlocking(
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
				return PaginatedListIterator[EncryptedCalendarItem](
					producer = class_pointer,
					deserializer = lambda x: EncryptedCalendarItem._deserialize(x),
					executor = self.cardinal_sdk._executor
				)

		async def filter_calendar_items_by_sorted_async(self, filter: SortableFilterOptions[CalendarItem]) -> PaginatedListIterator[EncryptedCalendarItem]:
			def do_decode(raw_result):
				return PaginatedListIterator[EncryptedCalendarItem](
					producer = raw_result,
					deserializer = lambda x: EncryptedCalendarItem._deserialize(x),
					executor = self.cardinal_sdk._executor
				)
			payload = {
				"filter": filter.__serialize__(),
			}
			return await execute_async_method_job(
				self.cardinal_sdk._executor,
				False,
				do_decode,
				symbols.kotlin.root.com.icure.cardinal.sdk.py.api.CalendarItemApi.encrypted.filterCalendarItemsBySortedAsync,
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)

		def filter_calendar_items_by_sorted_blocking(self, filter: SortableFilterOptions[CalendarItem]) -> PaginatedListIterator[EncryptedCalendarItem]:
			payload = {
				"filter": filter.__serialize__(),
			}
			call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.CalendarItemApi.encrypted.filterCalendarItemsBySortedBlocking(
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
				return PaginatedListIterator[EncryptedCalendarItem](
					producer = class_pointer,
					deserializer = lambda x: EncryptedCalendarItem._deserialize(x),
					executor = self.cardinal_sdk._executor
				)

		async def undelete_calendar_item_by_id_async(self, id: str, rev: str) -> EncryptedCalendarItem:
			def do_decode(raw_result):
				return EncryptedCalendarItem._deserialize(raw_result)
			payload = {
				"id": id,
				"rev": rev,
			}
			return await execute_async_method_job(
				self.cardinal_sdk._executor,
				True,
				do_decode,
				symbols.kotlin.root.com.icure.cardinal.sdk.py.api.CalendarItemApi.encrypted.undeleteCalendarItemByIdAsync,
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)

		def undelete_calendar_item_by_id_blocking(self, id: str, rev: str) -> EncryptedCalendarItem:
			payload = {
				"id": id,
				"rev": rev,
			}
			call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.CalendarItemApi.encrypted.undeleteCalendarItemByIdBlocking(
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)
			result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
			symbols.DisposeString(call_result)
			if result_info.failure is not None:
				raise interpret_kt_error(result_info.failure)
			else:
				return_value = EncryptedCalendarItem._deserialize(result_info.success)
				return return_value

		async def undelete_calendar_item_async(self, calendar_item: CalendarItem) -> EncryptedCalendarItem:
			def do_decode(raw_result):
				return EncryptedCalendarItem._deserialize(raw_result)
			payload = {
				"calendarItem": serialize_calendar_item(calendar_item),
			}
			return await execute_async_method_job(
				self.cardinal_sdk._executor,
				True,
				do_decode,
				symbols.kotlin.root.com.icure.cardinal.sdk.py.api.CalendarItemApi.encrypted.undeleteCalendarItemAsync,
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)

		def undelete_calendar_item_blocking(self, calendar_item: CalendarItem) -> EncryptedCalendarItem:
			payload = {
				"calendarItem": serialize_calendar_item(calendar_item),
			}
			call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.CalendarItemApi.encrypted.undeleteCalendarItemBlocking(
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)
			result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
			symbols.DisposeString(call_result)
			if result_info.failure is not None:
				raise interpret_kt_error(result_info.failure)
			else:
				return_value = EncryptedCalendarItem._deserialize(result_info.success)
				return return_value

		async def modify_calendar_item_async(self, entity: EncryptedCalendarItem) -> EncryptedCalendarItem:
			def do_decode(raw_result):
				return EncryptedCalendarItem._deserialize(raw_result)
			payload = {
				"entity": entity.__serialize__(),
			}
			return await execute_async_method_job(
				self.cardinal_sdk._executor,
				True,
				do_decode,
				symbols.kotlin.root.com.icure.cardinal.sdk.py.api.CalendarItemApi.encrypted.modifyCalendarItemAsync,
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)

		def modify_calendar_item_blocking(self, entity: EncryptedCalendarItem) -> EncryptedCalendarItem:
			payload = {
				"entity": entity.__serialize__(),
			}
			call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.CalendarItemApi.encrypted.modifyCalendarItemBlocking(
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)
			result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
			symbols.DisposeString(call_result)
			if result_info.failure is not None:
				raise interpret_kt_error(result_info.failure)
			else:
				return_value = EncryptedCalendarItem._deserialize(result_info.success)
				return return_value

		async def get_calendar_item_async(self, entity_id: str) -> EncryptedCalendarItem:
			def do_decode(raw_result):
				return EncryptedCalendarItem._deserialize(raw_result)
			payload = {
				"entityId": entity_id,
			}
			return await execute_async_method_job(
				self.cardinal_sdk._executor,
				True,
				do_decode,
				symbols.kotlin.root.com.icure.cardinal.sdk.py.api.CalendarItemApi.encrypted.getCalendarItemAsync,
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)

		def get_calendar_item_blocking(self, entity_id: str) -> EncryptedCalendarItem:
			payload = {
				"entityId": entity_id,
			}
			call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.CalendarItemApi.encrypted.getCalendarItemBlocking(
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)
			result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
			symbols.DisposeString(call_result)
			if result_info.failure is not None:
				raise interpret_kt_error(result_info.failure)
			else:
				return_value = EncryptedCalendarItem._deserialize(result_info.success)
				return return_value

		async def get_calendar_items_async(self, entity_ids: List[str]) -> List[EncryptedCalendarItem]:
			def do_decode(raw_result):
				return [EncryptedCalendarItem._deserialize(x1) for x1 in raw_result]
			payload = {
				"entityIds": [x0 for x0 in entity_ids],
			}
			return await execute_async_method_job(
				self.cardinal_sdk._executor,
				True,
				do_decode,
				symbols.kotlin.root.com.icure.cardinal.sdk.py.api.CalendarItemApi.encrypted.getCalendarItemsAsync,
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)

		def get_calendar_items_blocking(self, entity_ids: List[str]) -> List[EncryptedCalendarItem]:
			payload = {
				"entityIds": [x0 for x0 in entity_ids],
			}
			call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.CalendarItemApi.encrypted.getCalendarItemsBlocking(
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)
			result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
			symbols.DisposeString(call_result)
			if result_info.failure is not None:
				raise interpret_kt_error(result_info.failure)
			else:
				return_value = [EncryptedCalendarItem._deserialize(x1) for x1 in result_info.success]
				return return_value

	class CalendarItemFlavouredApi:

		def __init__(self, cardinal_sdk):
			self.cardinal_sdk = cardinal_sdk

		async def share_with_async(self, delegate_id: str, calendar_item: CalendarItem, options: Optional[CalendarItemShareOptions] = None) -> CalendarItem:
			def do_decode(raw_result):
				return deserialize_calendar_item(raw_result)
			payload = {
				"delegateId": delegate_id,
				"calendarItem": serialize_calendar_item(calendar_item),
				"options": options.__serialize__() if options is not None else None,
			}
			return await execute_async_method_job(
				self.cardinal_sdk._executor,
				True,
				do_decode,
				symbols.kotlin.root.com.icure.cardinal.sdk.py.api.CalendarItemApi.tryAndRecover.shareWithAsync,
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)

		def share_with_blocking(self, delegate_id: str, calendar_item: CalendarItem, options: Optional[CalendarItemShareOptions] = None) -> CalendarItem:
			payload = {
				"delegateId": delegate_id,
				"calendarItem": serialize_calendar_item(calendar_item),
				"options": options.__serialize__() if options is not None else None,
			}
			call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.CalendarItemApi.tryAndRecover.shareWithBlocking(
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)
			result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
			symbols.DisposeString(call_result)
			if result_info.failure is not None:
				raise interpret_kt_error(result_info.failure)
			else:
				return_value = deserialize_calendar_item(result_info.success)
				return return_value

		async def share_with_many_async(self, calendar_item: CalendarItem, delegates: Dict[str, CalendarItemShareOptions]) -> CalendarItem:
			def do_decode(raw_result):
				return deserialize_calendar_item(raw_result)
			payload = {
				"calendarItem": serialize_calendar_item(calendar_item),
				"delegates": {k0: v0.__serialize__() for k0, v0 in delegates.items()},
			}
			return await execute_async_method_job(
				self.cardinal_sdk._executor,
				True,
				do_decode,
				symbols.kotlin.root.com.icure.cardinal.sdk.py.api.CalendarItemApi.tryAndRecover.shareWithManyAsync,
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)

		def share_with_many_blocking(self, calendar_item: CalendarItem, delegates: Dict[str, CalendarItemShareOptions]) -> CalendarItem:
			payload = {
				"calendarItem": serialize_calendar_item(calendar_item),
				"delegates": {k0: v0.__serialize__() for k0, v0 in delegates.items()},
			}
			call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.CalendarItemApi.tryAndRecover.shareWithManyBlocking(
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)
			result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
			symbols.DisposeString(call_result)
			if result_info.failure is not None:
				raise interpret_kt_error(result_info.failure)
			else:
				return_value = deserialize_calendar_item(result_info.success)
				return return_value

		async def link_to_patient_async(self, calendar_item: CalendarItem, patient: Patient, share_link_with_delegates: List[str]) -> CalendarItem:
			def do_decode(raw_result):
				return deserialize_calendar_item(raw_result)
			payload = {
				"calendarItem": serialize_calendar_item(calendar_item),
				"patient": serialize_patient(patient),
				"shareLinkWithDelegates": [x0 for x0 in share_link_with_delegates],
			}
			return await execute_async_method_job(
				self.cardinal_sdk._executor,
				True,
				do_decode,
				symbols.kotlin.root.com.icure.cardinal.sdk.py.api.CalendarItemApi.tryAndRecover.linkToPatientAsync,
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)

		def link_to_patient_blocking(self, calendar_item: CalendarItem, patient: Patient, share_link_with_delegates: List[str]) -> CalendarItem:
			payload = {
				"calendarItem": serialize_calendar_item(calendar_item),
				"patient": serialize_patient(patient),
				"shareLinkWithDelegates": [x0 for x0 in share_link_with_delegates],
			}
			call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.CalendarItemApi.tryAndRecover.linkToPatientBlocking(
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)
			result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
			symbols.DisposeString(call_result)
			if result_info.failure is not None:
				raise interpret_kt_error(result_info.failure)
			else:
				return_value = deserialize_calendar_item(result_info.success)
				return return_value

		async def filter_calendar_items_by_async(self, filter: FilterOptions[CalendarItem]) -> PaginatedListIterator[CalendarItem]:
			def do_decode(raw_result):
				return PaginatedListIterator[CalendarItem](
					producer = raw_result,
					deserializer = lambda x: deserialize_calendar_item(x),
					executor = self.cardinal_sdk._executor
				)
			payload = {
				"filter": filter.__serialize__(),
			}
			return await execute_async_method_job(
				self.cardinal_sdk._executor,
				False,
				do_decode,
				symbols.kotlin.root.com.icure.cardinal.sdk.py.api.CalendarItemApi.tryAndRecover.filterCalendarItemsByAsync,
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)

		def filter_calendar_items_by_blocking(self, filter: FilterOptions[CalendarItem]) -> PaginatedListIterator[CalendarItem]:
			payload = {
				"filter": filter.__serialize__(),
			}
			call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.CalendarItemApi.tryAndRecover.filterCalendarItemsByBlocking(
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
				return PaginatedListIterator[CalendarItem](
					producer = class_pointer,
					deserializer = lambda x: deserialize_calendar_item(x),
					executor = self.cardinal_sdk._executor
				)

		async def filter_calendar_items_by_sorted_async(self, filter: SortableFilterOptions[CalendarItem]) -> PaginatedListIterator[CalendarItem]:
			def do_decode(raw_result):
				return PaginatedListIterator[CalendarItem](
					producer = raw_result,
					deserializer = lambda x: deserialize_calendar_item(x),
					executor = self.cardinal_sdk._executor
				)
			payload = {
				"filter": filter.__serialize__(),
			}
			return await execute_async_method_job(
				self.cardinal_sdk._executor,
				False,
				do_decode,
				symbols.kotlin.root.com.icure.cardinal.sdk.py.api.CalendarItemApi.tryAndRecover.filterCalendarItemsBySortedAsync,
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)

		def filter_calendar_items_by_sorted_blocking(self, filter: SortableFilterOptions[CalendarItem]) -> PaginatedListIterator[CalendarItem]:
			payload = {
				"filter": filter.__serialize__(),
			}
			call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.CalendarItemApi.tryAndRecover.filterCalendarItemsBySortedBlocking(
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
				return PaginatedListIterator[CalendarItem](
					producer = class_pointer,
					deserializer = lambda x: deserialize_calendar_item(x),
					executor = self.cardinal_sdk._executor
				)

		async def undelete_calendar_item_by_id_async(self, id: str, rev: str) -> CalendarItem:
			def do_decode(raw_result):
				return deserialize_calendar_item(raw_result)
			payload = {
				"id": id,
				"rev": rev,
			}
			return await execute_async_method_job(
				self.cardinal_sdk._executor,
				True,
				do_decode,
				symbols.kotlin.root.com.icure.cardinal.sdk.py.api.CalendarItemApi.tryAndRecover.undeleteCalendarItemByIdAsync,
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)

		def undelete_calendar_item_by_id_blocking(self, id: str, rev: str) -> CalendarItem:
			payload = {
				"id": id,
				"rev": rev,
			}
			call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.CalendarItemApi.tryAndRecover.undeleteCalendarItemByIdBlocking(
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)
			result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
			symbols.DisposeString(call_result)
			if result_info.failure is not None:
				raise interpret_kt_error(result_info.failure)
			else:
				return_value = deserialize_calendar_item(result_info.success)
				return return_value

		async def undelete_calendar_item_async(self, calendar_item: CalendarItem) -> CalendarItem:
			def do_decode(raw_result):
				return deserialize_calendar_item(raw_result)
			payload = {
				"calendarItem": serialize_calendar_item(calendar_item),
			}
			return await execute_async_method_job(
				self.cardinal_sdk._executor,
				True,
				do_decode,
				symbols.kotlin.root.com.icure.cardinal.sdk.py.api.CalendarItemApi.tryAndRecover.undeleteCalendarItemAsync,
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)

		def undelete_calendar_item_blocking(self, calendar_item: CalendarItem) -> CalendarItem:
			payload = {
				"calendarItem": serialize_calendar_item(calendar_item),
			}
			call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.CalendarItemApi.tryAndRecover.undeleteCalendarItemBlocking(
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)
			result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
			symbols.DisposeString(call_result)
			if result_info.failure is not None:
				raise interpret_kt_error(result_info.failure)
			else:
				return_value = deserialize_calendar_item(result_info.success)
				return return_value

		async def modify_calendar_item_async(self, entity: CalendarItem) -> CalendarItem:
			def do_decode(raw_result):
				return deserialize_calendar_item(raw_result)
			payload = {
				"entity": serialize_calendar_item(entity),
			}
			return await execute_async_method_job(
				self.cardinal_sdk._executor,
				True,
				do_decode,
				symbols.kotlin.root.com.icure.cardinal.sdk.py.api.CalendarItemApi.tryAndRecover.modifyCalendarItemAsync,
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)

		def modify_calendar_item_blocking(self, entity: CalendarItem) -> CalendarItem:
			payload = {
				"entity": serialize_calendar_item(entity),
			}
			call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.CalendarItemApi.tryAndRecover.modifyCalendarItemBlocking(
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)
			result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
			symbols.DisposeString(call_result)
			if result_info.failure is not None:
				raise interpret_kt_error(result_info.failure)
			else:
				return_value = deserialize_calendar_item(result_info.success)
				return return_value

		async def get_calendar_item_async(self, entity_id: str) -> CalendarItem:
			def do_decode(raw_result):
				return deserialize_calendar_item(raw_result)
			payload = {
				"entityId": entity_id,
			}
			return await execute_async_method_job(
				self.cardinal_sdk._executor,
				True,
				do_decode,
				symbols.kotlin.root.com.icure.cardinal.sdk.py.api.CalendarItemApi.tryAndRecover.getCalendarItemAsync,
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)

		def get_calendar_item_blocking(self, entity_id: str) -> CalendarItem:
			payload = {
				"entityId": entity_id,
			}
			call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.CalendarItemApi.tryAndRecover.getCalendarItemBlocking(
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)
			result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
			symbols.DisposeString(call_result)
			if result_info.failure is not None:
				raise interpret_kt_error(result_info.failure)
			else:
				return_value = deserialize_calendar_item(result_info.success)
				return return_value

		async def get_calendar_items_async(self, entity_ids: List[str]) -> List[CalendarItem]:
			def do_decode(raw_result):
				return [deserialize_calendar_item(x1) for x1 in raw_result]
			payload = {
				"entityIds": [x0 for x0 in entity_ids],
			}
			return await execute_async_method_job(
				self.cardinal_sdk._executor,
				True,
				do_decode,
				symbols.kotlin.root.com.icure.cardinal.sdk.py.api.CalendarItemApi.tryAndRecover.getCalendarItemsAsync,
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)

		def get_calendar_items_blocking(self, entity_ids: List[str]) -> List[CalendarItem]:
			payload = {
				"entityIds": [x0 for x0 in entity_ids],
			}
			call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.CalendarItemApi.tryAndRecover.getCalendarItemsBlocking(
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)
			result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
			symbols.DisposeString(call_result)
			if result_info.failure is not None:
				raise interpret_kt_error(result_info.failure)
			else:
				return_value = [deserialize_calendar_item(x1) for x1 in result_info.success]
				return return_value

	def __init__(self, cardinal_sdk):
		self.cardinal_sdk = cardinal_sdk
		self.encrypted = CalendarItemApi.CalendarItemFlavouredEncryptedApi(self.cardinal_sdk)
		self.try_and_recover = CalendarItemApi.CalendarItemFlavouredApi(self.cardinal_sdk)

	async def create_calendar_item_async(self, entity: DecryptedCalendarItem) -> DecryptedCalendarItem:
		def do_decode(raw_result):
			return DecryptedCalendarItem._deserialize(raw_result)
		payload = {
			"entity": entity.__serialize__(),
		}
		return await execute_async_method_job(
			self.cardinal_sdk._executor,
			True,
			do_decode,
			symbols.kotlin.root.com.icure.cardinal.sdk.py.api.CalendarItemApi.createCalendarItemAsync,
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)

	def create_calendar_item_blocking(self, entity: DecryptedCalendarItem) -> DecryptedCalendarItem:
		payload = {
			"entity": entity.__serialize__(),
		}
		call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.CalendarItemApi.createCalendarItemBlocking(
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)
		result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
		symbols.DisposeString(call_result)
		if result_info.failure is not None:
			raise interpret_kt_error(result_info.failure)
		else:
			return_value = DecryptedCalendarItem._deserialize(result_info.success)
			return return_value

	async def with_encryption_metadata_async(self, base: Optional[DecryptedCalendarItem], patient: Patient, user: Optional[User] = None, delegates: Dict[str, AccessLevel] = {}, secret_id: SecretIdUseOption = SecretIdUseOptionUseAnySharedWithParent()) -> DecryptedCalendarItem:
		def do_decode(raw_result):
			return DecryptedCalendarItem._deserialize(raw_result)
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
			symbols.kotlin.root.com.icure.cardinal.sdk.py.api.CalendarItemApi.withEncryptionMetadataAsync,
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)

	def with_encryption_metadata_blocking(self, base: Optional[DecryptedCalendarItem], patient: Patient, user: Optional[User] = None, delegates: Dict[str, AccessLevel] = {}, secret_id: SecretIdUseOption = SecretIdUseOptionUseAnySharedWithParent()) -> DecryptedCalendarItem:
		payload = {
			"base": base.__serialize__() if base is not None else None,
			"patient": serialize_patient(patient),
			"user": user.__serialize__() if user is not None else None,
			"delegates": {k0: v0.__serialize__() for k0, v0 in delegates.items()},
			"secretId": serialize_secret_id_use_option(secret_id),
		}
		call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.CalendarItemApi.withEncryptionMetadataBlocking(
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)
		result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
		symbols.DisposeString(call_result)
		if result_info.failure is not None:
			raise interpret_kt_error(result_info.failure)
		else:
			return_value = DecryptedCalendarItem._deserialize(result_info.success)
			return return_value

	async def get_encryption_keys_of_async(self, calendar_item: CalendarItem) -> List[HexString]:
		def do_decode(raw_result):
			return [x1 for x1 in raw_result]
		payload = {
			"calendarItem": serialize_calendar_item(calendar_item),
		}
		return await execute_async_method_job(
			self.cardinal_sdk._executor,
			True,
			do_decode,
			symbols.kotlin.root.com.icure.cardinal.sdk.py.api.CalendarItemApi.getEncryptionKeysOfAsync,
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)

	def get_encryption_keys_of_blocking(self, calendar_item: CalendarItem) -> List[HexString]:
		payload = {
			"calendarItem": serialize_calendar_item(calendar_item),
		}
		call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.CalendarItemApi.getEncryptionKeysOfBlocking(
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

	async def has_write_access_async(self, calendar_item: CalendarItem) -> bool:
		def do_decode(raw_result):
			return raw_result
		payload = {
			"calendarItem": serialize_calendar_item(calendar_item),
		}
		return await execute_async_method_job(
			self.cardinal_sdk._executor,
			True,
			do_decode,
			symbols.kotlin.root.com.icure.cardinal.sdk.py.api.CalendarItemApi.hasWriteAccessAsync,
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)

	def has_write_access_blocking(self, calendar_item: CalendarItem) -> bool:
		payload = {
			"calendarItem": serialize_calendar_item(calendar_item),
		}
		call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.CalendarItemApi.hasWriteAccessBlocking(
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

	async def decrypt_patient_id_of_async(self, calendar_item: CalendarItem) -> List[str]:
		def do_decode(raw_result):
			return [x1 for x1 in raw_result]
		payload = {
			"calendarItem": serialize_calendar_item(calendar_item),
		}
		return await execute_async_method_job(
			self.cardinal_sdk._executor,
			True,
			do_decode,
			symbols.kotlin.root.com.icure.cardinal.sdk.py.api.CalendarItemApi.decryptPatientIdOfAsync,
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)

	def decrypt_patient_id_of_blocking(self, calendar_item: CalendarItem) -> List[str]:
		payload = {
			"calendarItem": serialize_calendar_item(calendar_item),
		}
		call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.CalendarItemApi.decryptPatientIdOfBlocking(
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

	async def create_delegation_de_anonymization_metadata_async(self, entity: CalendarItem, delegates: List[str]) -> None:
		def do_decode(raw_result):
			return raw_result
		payload = {
			"entity": serialize_calendar_item(entity),
			"delegates": [x0 for x0 in delegates],
		}
		return await execute_async_method_job(
			self.cardinal_sdk._executor,
			True,
			do_decode,
			symbols.kotlin.root.com.icure.cardinal.sdk.py.api.CalendarItemApi.createDelegationDeAnonymizationMetadataAsync,
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)

	def create_delegation_de_anonymization_metadata_blocking(self, entity: CalendarItem, delegates: List[str]) -> None:
		payload = {
			"entity": serialize_calendar_item(entity),
			"delegates": [x0 for x0 in delegates],
		}
		call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.CalendarItemApi.createDelegationDeAnonymizationMetadataBlocking(
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)
		result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
		symbols.DisposeString(call_result)
		if result_info.failure is not None:
			raise interpret_kt_error(result_info.failure)

	async def decrypt_async(self, calendar_item: EncryptedCalendarItem) -> DecryptedCalendarItem:
		def do_decode(raw_result):
			return DecryptedCalendarItem._deserialize(raw_result)
		payload = {
			"calendarItem": calendar_item.__serialize__(),
		}
		return await execute_async_method_job(
			self.cardinal_sdk._executor,
			True,
			do_decode,
			symbols.kotlin.root.com.icure.cardinal.sdk.py.api.CalendarItemApi.decryptAsync,
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)

	def decrypt_blocking(self, calendar_item: EncryptedCalendarItem) -> DecryptedCalendarItem:
		payload = {
			"calendarItem": calendar_item.__serialize__(),
		}
		call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.CalendarItemApi.decryptBlocking(
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)
		result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
		symbols.DisposeString(call_result)
		if result_info.failure is not None:
			raise interpret_kt_error(result_info.failure)
		else:
			return_value = DecryptedCalendarItem._deserialize(result_info.success)
			return return_value

	async def try_decrypt_async(self, calendar_item: EncryptedCalendarItem) -> CalendarItem:
		def do_decode(raw_result):
			return deserialize_calendar_item(raw_result)
		payload = {
			"calendarItem": calendar_item.__serialize__(),
		}
		return await execute_async_method_job(
			self.cardinal_sdk._executor,
			True,
			do_decode,
			symbols.kotlin.root.com.icure.cardinal.sdk.py.api.CalendarItemApi.tryDecryptAsync,
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)

	def try_decrypt_blocking(self, calendar_item: EncryptedCalendarItem) -> CalendarItem:
		payload = {
			"calendarItem": calendar_item.__serialize__(),
		}
		call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.CalendarItemApi.tryDecryptBlocking(
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)
		result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
		symbols.DisposeString(call_result)
		if result_info.failure is not None:
			raise interpret_kt_error(result_info.failure)
		else:
			return_value = deserialize_calendar_item(result_info.success)
			return return_value

	async def match_calendar_items_by_async(self, filter: FilterOptions[CalendarItem]) -> List[str]:
		def do_decode(raw_result):
			return [x1 for x1 in raw_result]
		payload = {
			"filter": filter.__serialize__(),
		}
		return await execute_async_method_job(
			self.cardinal_sdk._executor,
			True,
			do_decode,
			symbols.kotlin.root.com.icure.cardinal.sdk.py.api.CalendarItemApi.matchCalendarItemsByAsync,
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)

	def match_calendar_items_by_blocking(self, filter: FilterOptions[CalendarItem]) -> List[str]:
		payload = {
			"filter": filter.__serialize__(),
		}
		call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.CalendarItemApi.matchCalendarItemsByBlocking(
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

	async def match_calendar_items_by_sorted_async(self, filter: SortableFilterOptions[CalendarItem]) -> List[str]:
		def do_decode(raw_result):
			return [x1 for x1 in raw_result]
		payload = {
			"filter": filter.__serialize__(),
		}
		return await execute_async_method_job(
			self.cardinal_sdk._executor,
			True,
			do_decode,
			symbols.kotlin.root.com.icure.cardinal.sdk.py.api.CalendarItemApi.matchCalendarItemsBySortedAsync,
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)

	def match_calendar_items_by_sorted_blocking(self, filter: SortableFilterOptions[CalendarItem]) -> List[str]:
		payload = {
			"filter": filter.__serialize__(),
		}
		call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.CalendarItemApi.matchCalendarItemsBySortedBlocking(
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

	async def delete_calendar_item_by_id_async(self, entity_id: str, rev: str) -> DocIdentifier:
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
			symbols.kotlin.root.com.icure.cardinal.sdk.py.api.CalendarItemApi.deleteCalendarItemByIdAsync,
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)

	def delete_calendar_item_by_id_blocking(self, entity_id: str, rev: str) -> DocIdentifier:
		payload = {
			"entityId": entity_id,
			"rev": rev,
		}
		call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.CalendarItemApi.deleteCalendarItemByIdBlocking(
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

	async def delete_calendar_items_by_ids_async(self, entity_ids: List[IdWithMandatoryRev]) -> List[DocIdentifier]:
		def do_decode(raw_result):
			return [DocIdentifier._deserialize(x1) for x1 in raw_result]
		payload = {
			"entityIds": [x0.__serialize__() for x0 in entity_ids],
		}
		return await execute_async_method_job(
			self.cardinal_sdk._executor,
			True,
			do_decode,
			symbols.kotlin.root.com.icure.cardinal.sdk.py.api.CalendarItemApi.deleteCalendarItemsByIdsAsync,
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)

	def delete_calendar_items_by_ids_blocking(self, entity_ids: List[IdWithMandatoryRev]) -> List[DocIdentifier]:
		payload = {
			"entityIds": [x0.__serialize__() for x0 in entity_ids],
		}
		call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.CalendarItemApi.deleteCalendarItemsByIdsBlocking(
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

	async def purge_calendar_item_by_id_async(self, id: str, rev: str) -> None:
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
			symbols.kotlin.root.com.icure.cardinal.sdk.py.api.CalendarItemApi.purgeCalendarItemByIdAsync,
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)

	def purge_calendar_item_by_id_blocking(self, id: str, rev: str) -> None:
		payload = {
			"id": id,
			"rev": rev,
		}
		call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.CalendarItemApi.purgeCalendarItemByIdBlocking(
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)
		result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
		symbols.DisposeString(call_result)
		if result_info.failure is not None:
			raise interpret_kt_error(result_info.failure)

	async def delete_calendar_item_async(self, calendar_item: CalendarItem) -> DocIdentifier:
		def do_decode(raw_result):
			return DocIdentifier._deserialize(raw_result)
		payload = {
			"calendarItem": serialize_calendar_item(calendar_item),
		}
		return await execute_async_method_job(
			self.cardinal_sdk._executor,
			True,
			do_decode,
			symbols.kotlin.root.com.icure.cardinal.sdk.py.api.CalendarItemApi.deleteCalendarItemAsync,
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)

	def delete_calendar_item_blocking(self, calendar_item: CalendarItem) -> DocIdentifier:
		payload = {
			"calendarItem": serialize_calendar_item(calendar_item),
		}
		call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.CalendarItemApi.deleteCalendarItemBlocking(
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

	async def delete_calendar_items_async(self, calendar_items: List[CalendarItem]) -> List[DocIdentifier]:
		def do_decode(raw_result):
			return [DocIdentifier._deserialize(x1) for x1 in raw_result]
		payload = {
			"calendarItems": [serialize_calendar_item(x0) for x0 in calendar_items],
		}
		return await execute_async_method_job(
			self.cardinal_sdk._executor,
			True,
			do_decode,
			symbols.kotlin.root.com.icure.cardinal.sdk.py.api.CalendarItemApi.deleteCalendarItemsAsync,
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)

	def delete_calendar_items_blocking(self, calendar_items: List[CalendarItem]) -> List[DocIdentifier]:
		payload = {
			"calendarItems": [serialize_calendar_item(x0) for x0 in calendar_items],
		}
		call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.CalendarItemApi.deleteCalendarItemsBlocking(
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

	async def purge_calendar_item_async(self, calendar_item: CalendarItem) -> None:
		def do_decode(raw_result):
			return raw_result
		payload = {
			"calendarItem": serialize_calendar_item(calendar_item),
		}
		return await execute_async_method_job(
			self.cardinal_sdk._executor,
			True,
			do_decode,
			symbols.kotlin.root.com.icure.cardinal.sdk.py.api.CalendarItemApi.purgeCalendarItemAsync,
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)

	def purge_calendar_item_blocking(self, calendar_item: CalendarItem) -> None:
		payload = {
			"calendarItem": serialize_calendar_item(calendar_item),
		}
		call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.CalendarItemApi.purgeCalendarItemBlocking(
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)
		result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
		symbols.DisposeString(call_result)
		if result_info.failure is not None:
			raise interpret_kt_error(result_info.failure)

	async def share_with_async(self, delegate_id: str, calendar_item: DecryptedCalendarItem, options: Optional[CalendarItemShareOptions] = None) -> DecryptedCalendarItem:
		def do_decode(raw_result):
			return DecryptedCalendarItem._deserialize(raw_result)
		payload = {
			"delegateId": delegate_id,
			"calendarItem": calendar_item.__serialize__(),
			"options": options.__serialize__() if options is not None else None,
		}
		return await execute_async_method_job(
			self.cardinal_sdk._executor,
			True,
			do_decode,
			symbols.kotlin.root.com.icure.cardinal.sdk.py.api.CalendarItemApi.shareWithAsync,
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)

	def share_with_blocking(self, delegate_id: str, calendar_item: DecryptedCalendarItem, options: Optional[CalendarItemShareOptions] = None) -> DecryptedCalendarItem:
		payload = {
			"delegateId": delegate_id,
			"calendarItem": calendar_item.__serialize__(),
			"options": options.__serialize__() if options is not None else None,
		}
		call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.CalendarItemApi.shareWithBlocking(
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)
		result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
		symbols.DisposeString(call_result)
		if result_info.failure is not None:
			raise interpret_kt_error(result_info.failure)
		else:
			return_value = DecryptedCalendarItem._deserialize(result_info.success)
			return return_value

	async def share_with_many_async(self, calendar_item: DecryptedCalendarItem, delegates: Dict[str, CalendarItemShareOptions]) -> DecryptedCalendarItem:
		def do_decode(raw_result):
			return DecryptedCalendarItem._deserialize(raw_result)
		payload = {
			"calendarItem": calendar_item.__serialize__(),
			"delegates": {k0: v0.__serialize__() for k0, v0 in delegates.items()},
		}
		return await execute_async_method_job(
			self.cardinal_sdk._executor,
			True,
			do_decode,
			symbols.kotlin.root.com.icure.cardinal.sdk.py.api.CalendarItemApi.shareWithManyAsync,
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)

	def share_with_many_blocking(self, calendar_item: DecryptedCalendarItem, delegates: Dict[str, CalendarItemShareOptions]) -> DecryptedCalendarItem:
		payload = {
			"calendarItem": calendar_item.__serialize__(),
			"delegates": {k0: v0.__serialize__() for k0, v0 in delegates.items()},
		}
		call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.CalendarItemApi.shareWithManyBlocking(
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)
		result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
		symbols.DisposeString(call_result)
		if result_info.failure is not None:
			raise interpret_kt_error(result_info.failure)
		else:
			return_value = DecryptedCalendarItem._deserialize(result_info.success)
			return return_value

	async def link_to_patient_async(self, calendar_item: CalendarItem, patient: Patient, share_link_with_delegates: List[str]) -> DecryptedCalendarItem:
		def do_decode(raw_result):
			return DecryptedCalendarItem._deserialize(raw_result)
		payload = {
			"calendarItem": serialize_calendar_item(calendar_item),
			"patient": serialize_patient(patient),
			"shareLinkWithDelegates": [x0 for x0 in share_link_with_delegates],
		}
		return await execute_async_method_job(
			self.cardinal_sdk._executor,
			True,
			do_decode,
			symbols.kotlin.root.com.icure.cardinal.sdk.py.api.CalendarItemApi.linkToPatientAsync,
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)

	def link_to_patient_blocking(self, calendar_item: CalendarItem, patient: Patient, share_link_with_delegates: List[str]) -> DecryptedCalendarItem:
		payload = {
			"calendarItem": serialize_calendar_item(calendar_item),
			"patient": serialize_patient(patient),
			"shareLinkWithDelegates": [x0 for x0 in share_link_with_delegates],
		}
		call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.CalendarItemApi.linkToPatientBlocking(
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)
		result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
		symbols.DisposeString(call_result)
		if result_info.failure is not None:
			raise interpret_kt_error(result_info.failure)
		else:
			return_value = DecryptedCalendarItem._deserialize(result_info.success)
			return return_value

	async def filter_calendar_items_by_async(self, filter: FilterOptions[CalendarItem]) -> PaginatedListIterator[DecryptedCalendarItem]:
		def do_decode(raw_result):
			return PaginatedListIterator[DecryptedCalendarItem](
				producer = raw_result,
				deserializer = lambda x: DecryptedCalendarItem._deserialize(x),
				executor = self.cardinal_sdk._executor
			)
		payload = {
			"filter": filter.__serialize__(),
		}
		return await execute_async_method_job(
			self.cardinal_sdk._executor,
			False,
			do_decode,
			symbols.kotlin.root.com.icure.cardinal.sdk.py.api.CalendarItemApi.filterCalendarItemsByAsync,
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)

	def filter_calendar_items_by_blocking(self, filter: FilterOptions[CalendarItem]) -> PaginatedListIterator[DecryptedCalendarItem]:
		payload = {
			"filter": filter.__serialize__(),
		}
		call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.CalendarItemApi.filterCalendarItemsByBlocking(
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
			return PaginatedListIterator[DecryptedCalendarItem](
				producer = class_pointer,
				deserializer = lambda x: DecryptedCalendarItem._deserialize(x),
				executor = self.cardinal_sdk._executor
			)

	async def filter_calendar_items_by_sorted_async(self, filter: SortableFilterOptions[CalendarItem]) -> PaginatedListIterator[DecryptedCalendarItem]:
		def do_decode(raw_result):
			return PaginatedListIterator[DecryptedCalendarItem](
				producer = raw_result,
				deserializer = lambda x: DecryptedCalendarItem._deserialize(x),
				executor = self.cardinal_sdk._executor
			)
		payload = {
			"filter": filter.__serialize__(),
		}
		return await execute_async_method_job(
			self.cardinal_sdk._executor,
			False,
			do_decode,
			symbols.kotlin.root.com.icure.cardinal.sdk.py.api.CalendarItemApi.filterCalendarItemsBySortedAsync,
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)

	def filter_calendar_items_by_sorted_blocking(self, filter: SortableFilterOptions[CalendarItem]) -> PaginatedListIterator[DecryptedCalendarItem]:
		payload = {
			"filter": filter.__serialize__(),
		}
		call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.CalendarItemApi.filterCalendarItemsBySortedBlocking(
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
			return PaginatedListIterator[DecryptedCalendarItem](
				producer = class_pointer,
				deserializer = lambda x: DecryptedCalendarItem._deserialize(x),
				executor = self.cardinal_sdk._executor
			)

	async def undelete_calendar_item_by_id_async(self, id: str, rev: str) -> DecryptedCalendarItem:
		def do_decode(raw_result):
			return DecryptedCalendarItem._deserialize(raw_result)
		payload = {
			"id": id,
			"rev": rev,
		}
		return await execute_async_method_job(
			self.cardinal_sdk._executor,
			True,
			do_decode,
			symbols.kotlin.root.com.icure.cardinal.sdk.py.api.CalendarItemApi.undeleteCalendarItemByIdAsync,
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)

	def undelete_calendar_item_by_id_blocking(self, id: str, rev: str) -> DecryptedCalendarItem:
		payload = {
			"id": id,
			"rev": rev,
		}
		call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.CalendarItemApi.undeleteCalendarItemByIdBlocking(
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)
		result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
		symbols.DisposeString(call_result)
		if result_info.failure is not None:
			raise interpret_kt_error(result_info.failure)
		else:
			return_value = DecryptedCalendarItem._deserialize(result_info.success)
			return return_value

	async def undelete_calendar_item_async(self, calendar_item: CalendarItem) -> DecryptedCalendarItem:
		def do_decode(raw_result):
			return DecryptedCalendarItem._deserialize(raw_result)
		payload = {
			"calendarItem": serialize_calendar_item(calendar_item),
		}
		return await execute_async_method_job(
			self.cardinal_sdk._executor,
			True,
			do_decode,
			symbols.kotlin.root.com.icure.cardinal.sdk.py.api.CalendarItemApi.undeleteCalendarItemAsync,
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)

	def undelete_calendar_item_blocking(self, calendar_item: CalendarItem) -> DecryptedCalendarItem:
		payload = {
			"calendarItem": serialize_calendar_item(calendar_item),
		}
		call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.CalendarItemApi.undeleteCalendarItemBlocking(
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)
		result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
		symbols.DisposeString(call_result)
		if result_info.failure is not None:
			raise interpret_kt_error(result_info.failure)
		else:
			return_value = DecryptedCalendarItem._deserialize(result_info.success)
			return return_value

	async def modify_calendar_item_async(self, entity: DecryptedCalendarItem) -> DecryptedCalendarItem:
		def do_decode(raw_result):
			return DecryptedCalendarItem._deserialize(raw_result)
		payload = {
			"entity": entity.__serialize__(),
		}
		return await execute_async_method_job(
			self.cardinal_sdk._executor,
			True,
			do_decode,
			symbols.kotlin.root.com.icure.cardinal.sdk.py.api.CalendarItemApi.modifyCalendarItemAsync,
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)

	def modify_calendar_item_blocking(self, entity: DecryptedCalendarItem) -> DecryptedCalendarItem:
		payload = {
			"entity": entity.__serialize__(),
		}
		call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.CalendarItemApi.modifyCalendarItemBlocking(
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)
		result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
		symbols.DisposeString(call_result)
		if result_info.failure is not None:
			raise interpret_kt_error(result_info.failure)
		else:
			return_value = DecryptedCalendarItem._deserialize(result_info.success)
			return return_value

	async def get_calendar_item_async(self, entity_id: str) -> DecryptedCalendarItem:
		def do_decode(raw_result):
			return DecryptedCalendarItem._deserialize(raw_result)
		payload = {
			"entityId": entity_id,
		}
		return await execute_async_method_job(
			self.cardinal_sdk._executor,
			True,
			do_decode,
			symbols.kotlin.root.com.icure.cardinal.sdk.py.api.CalendarItemApi.getCalendarItemAsync,
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)

	def get_calendar_item_blocking(self, entity_id: str) -> DecryptedCalendarItem:
		payload = {
			"entityId": entity_id,
		}
		call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.CalendarItemApi.getCalendarItemBlocking(
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)
		result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
		symbols.DisposeString(call_result)
		if result_info.failure is not None:
			raise interpret_kt_error(result_info.failure)
		else:
			return_value = DecryptedCalendarItem._deserialize(result_info.success)
			return return_value

	async def get_calendar_items_async(self, entity_ids: List[str]) -> List[DecryptedCalendarItem]:
		def do_decode(raw_result):
			return [DecryptedCalendarItem._deserialize(x1) for x1 in raw_result]
		payload = {
			"entityIds": [x0 for x0 in entity_ids],
		}
		return await execute_async_method_job(
			self.cardinal_sdk._executor,
			True,
			do_decode,
			symbols.kotlin.root.com.icure.cardinal.sdk.py.api.CalendarItemApi.getCalendarItemsAsync,
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)

	def get_calendar_items_blocking(self, entity_ids: List[str]) -> List[DecryptedCalendarItem]:
		payload = {
			"entityIds": [x0 for x0 in entity_ids],
		}
		call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.CalendarItemApi.getCalendarItemsBlocking(
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)
		result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
		symbols.DisposeString(call_result)
		if result_info.failure is not None:
			raise interpret_kt_error(result_info.failure)
		else:
			return_value = [DecryptedCalendarItem._deserialize(x1) for x1 in result_info.success]
			return return_value

	async def subscribe_to_events_async(self, events: List[SubscriptionEventType], filter: FilterOptions[CalendarItem], subscription_config: Optional[EntitySubscriptionConfiguration] = None) -> EntitySubscription[EncryptedCalendarItem]:
		def do_decode(raw_result):
			return EntitySubscription[EncryptedCalendarItem](
				producer = raw_result,
				deserializer = lambda x: EncryptedCalendarItem._deserialize(x),
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
			symbols.kotlin.root.com.icure.cardinal.sdk.py.api.CalendarItemApi.subscribeToEventsAsync,
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)

	def subscribe_to_events_blocking(self, events: List[SubscriptionEventType], filter: FilterOptions[CalendarItem], subscription_config: Optional[EntitySubscriptionConfiguration] = None) -> EntitySubscription[EncryptedCalendarItem]:
		payload = {
			"events": [x0.__serialize__() for x0 in events],
			"filter": filter.__serialize__(),
			"subscriptionConfig": subscription_config.__serialize__() if subscription_config is not None else None,
		}
		call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.CalendarItemApi.subscribeToEventsBlocking(
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
			return EntitySubscription[EncryptedCalendarItem](
				producer = class_pointer,
				deserializer = lambda x: EncryptedCalendarItem._deserialize(x),
				executor = self.cardinal_sdk._executor
			)
