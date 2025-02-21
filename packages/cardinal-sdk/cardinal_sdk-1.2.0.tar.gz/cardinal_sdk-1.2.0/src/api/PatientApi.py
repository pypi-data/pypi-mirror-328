# auto-generated file
import json
from cardinal_sdk.model import Patient, serialize_patient, DecryptedPatient, User, AccessLevel, EncryptedPatient, deserialize_patient, IdWithRev, ShareAllPatientDataOptions, DocIdentifier, IdWithMandatoryRev, EntityAccessInformation, PatientShareOptions, SubscriptionEventType, EntitySubscriptionConfiguration
from cardinal_sdk.async_utils import execute_async_method_job
from cardinal_sdk.kotlin_types import symbols
from typing import List, Optional, Dict
from cardinal_sdk.model.CallResult import create_result_from_json, interpret_kt_error
from ctypes import cast, c_char_p
from cardinal_sdk.model.specializations import HexString
from cardinal_sdk.filters.FilterOptions import FilterOptions, SortableFilterOptions
from cardinal_sdk.pagination.PaginatedListIterator import PaginatedListIterator
from cardinal_sdk.subscription.EntitySubscription import EntitySubscription


class PatientApi:

	class PatientFlavouredEncryptedApi:

		def __init__(self, cardinal_sdk):
			self.cardinal_sdk = cardinal_sdk

		async def share_with_async(self, delegate_id: str, patient: EncryptedPatient, options: Optional[PatientShareOptions] = None) -> EncryptedPatient:
			def do_decode(raw_result):
				return EncryptedPatient._deserialize(raw_result)
			payload = {
				"delegateId": delegate_id,
				"patient": patient.__serialize__(),
				"options": options.__serialize__() if options is not None else None,
			}
			return await execute_async_method_job(
				self.cardinal_sdk._executor,
				True,
				do_decode,
				symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.encrypted.shareWithAsync,
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)

		def share_with_blocking(self, delegate_id: str, patient: EncryptedPatient, options: Optional[PatientShareOptions] = None) -> EncryptedPatient:
			payload = {
				"delegateId": delegate_id,
				"patient": patient.__serialize__(),
				"options": options.__serialize__() if options is not None else None,
			}
			call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.encrypted.shareWithBlocking(
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)
			result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
			symbols.DisposeString(call_result)
			if result_info.failure is not None:
				raise interpret_kt_error(result_info.failure)
			else:
				return_value = EncryptedPatient._deserialize(result_info.success)
				return return_value

		async def share_with_many_async(self, patient: EncryptedPatient, delegates: Dict[str, PatientShareOptions]) -> EncryptedPatient:
			def do_decode(raw_result):
				return EncryptedPatient._deserialize(raw_result)
			payload = {
				"patient": patient.__serialize__(),
				"delegates": {k0: v0.__serialize__() for k0, v0 in delegates.items()},
			}
			return await execute_async_method_job(
				self.cardinal_sdk._executor,
				True,
				do_decode,
				symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.encrypted.shareWithManyAsync,
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)

		def share_with_many_blocking(self, patient: EncryptedPatient, delegates: Dict[str, PatientShareOptions]) -> EncryptedPatient:
			payload = {
				"patient": patient.__serialize__(),
				"delegates": {k0: v0.__serialize__() for k0, v0 in delegates.items()},
			}
			call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.encrypted.shareWithManyBlocking(
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)
			result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
			symbols.DisposeString(call_result)
			if result_info.failure is not None:
				raise interpret_kt_error(result_info.failure)
			else:
				return_value = EncryptedPatient._deserialize(result_info.success)
				return return_value

		async def initialize_confidential_secret_id_async(self, patient: EncryptedPatient) -> EncryptedPatient:
			def do_decode(raw_result):
				return EncryptedPatient._deserialize(raw_result)
			payload = {
				"patient": patient.__serialize__(),
			}
			return await execute_async_method_job(
				self.cardinal_sdk._executor,
				True,
				do_decode,
				symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.encrypted.initializeConfidentialSecretIdAsync,
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)

		def initialize_confidential_secret_id_blocking(self, patient: EncryptedPatient) -> EncryptedPatient:
			payload = {
				"patient": patient.__serialize__(),
			}
			call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.encrypted.initializeConfidentialSecretIdBlocking(
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)
			result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
			symbols.DisposeString(call_result)
			if result_info.failure is not None:
				raise interpret_kt_error(result_info.failure)
			else:
				return_value = EncryptedPatient._deserialize(result_info.success)
				return return_value

		async def filter_patients_by_async(self, filter: FilterOptions[Patient]) -> PaginatedListIterator[EncryptedPatient]:
			def do_decode(raw_result):
				return PaginatedListIterator[EncryptedPatient](
					producer = raw_result,
					deserializer = lambda x: EncryptedPatient._deserialize(x),
					executor = self.cardinal_sdk._executor
				)
			payload = {
				"filter": filter.__serialize__(),
			}
			return await execute_async_method_job(
				self.cardinal_sdk._executor,
				False,
				do_decode,
				symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.encrypted.filterPatientsByAsync,
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)

		def filter_patients_by_blocking(self, filter: FilterOptions[Patient]) -> PaginatedListIterator[EncryptedPatient]:
			payload = {
				"filter": filter.__serialize__(),
			}
			call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.encrypted.filterPatientsByBlocking(
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
				return PaginatedListIterator[EncryptedPatient](
					producer = class_pointer,
					deserializer = lambda x: EncryptedPatient._deserialize(x),
					executor = self.cardinal_sdk._executor
				)

		async def filter_patients_by_sorted_async(self, filter: SortableFilterOptions[Patient]) -> PaginatedListIterator[EncryptedPatient]:
			def do_decode(raw_result):
				return PaginatedListIterator[EncryptedPatient](
					producer = raw_result,
					deserializer = lambda x: EncryptedPatient._deserialize(x),
					executor = self.cardinal_sdk._executor
				)
			payload = {
				"filter": filter.__serialize__(),
			}
			return await execute_async_method_job(
				self.cardinal_sdk._executor,
				False,
				do_decode,
				symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.encrypted.filterPatientsBySortedAsync,
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)

		def filter_patients_by_sorted_blocking(self, filter: SortableFilterOptions[Patient]) -> PaginatedListIterator[EncryptedPatient]:
			payload = {
				"filter": filter.__serialize__(),
			}
			call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.encrypted.filterPatientsBySortedBlocking(
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
				return PaginatedListIterator[EncryptedPatient](
					producer = class_pointer,
					deserializer = lambda x: EncryptedPatient._deserialize(x),
					executor = self.cardinal_sdk._executor
				)

		async def undelete_patient_async(self, patient: Patient) -> Patient:
			def do_decode(raw_result):
				return deserialize_patient(raw_result)
			payload = {
				"patient": serialize_patient(patient),
			}
			return await execute_async_method_job(
				self.cardinal_sdk._executor,
				True,
				do_decode,
				symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.encrypted.undeletePatientAsync,
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)

		def undelete_patient_blocking(self, patient: Patient) -> Patient:
			payload = {
				"patient": serialize_patient(patient),
			}
			call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.encrypted.undeletePatientBlocking(
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)
			result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
			symbols.DisposeString(call_result)
			if result_info.failure is not None:
				raise interpret_kt_error(result_info.failure)
			else:
				return_value = deserialize_patient(result_info.success)
				return return_value

		async def modify_patient_async(self, entity: EncryptedPatient) -> EncryptedPatient:
			def do_decode(raw_result):
				return EncryptedPatient._deserialize(raw_result)
			payload = {
				"entity": entity.__serialize__(),
			}
			return await execute_async_method_job(
				self.cardinal_sdk._executor,
				True,
				do_decode,
				symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.encrypted.modifyPatientAsync,
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)

		def modify_patient_blocking(self, entity: EncryptedPatient) -> EncryptedPatient:
			payload = {
				"entity": entity.__serialize__(),
			}
			call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.encrypted.modifyPatientBlocking(
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)
			result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
			symbols.DisposeString(call_result)
			if result_info.failure is not None:
				raise interpret_kt_error(result_info.failure)
			else:
				return_value = EncryptedPatient._deserialize(result_info.success)
				return return_value

		async def undelete_patient_by_id_async(self, id: str, rev: str) -> EncryptedPatient:
			def do_decode(raw_result):
				return EncryptedPatient._deserialize(raw_result)
			payload = {
				"id": id,
				"rev": rev,
			}
			return await execute_async_method_job(
				self.cardinal_sdk._executor,
				True,
				do_decode,
				symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.encrypted.undeletePatientByIdAsync,
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)

		def undelete_patient_by_id_blocking(self, id: str, rev: str) -> EncryptedPatient:
			payload = {
				"id": id,
				"rev": rev,
			}
			call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.encrypted.undeletePatientByIdBlocking(
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)
			result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
			symbols.DisposeString(call_result)
			if result_info.failure is not None:
				raise interpret_kt_error(result_info.failure)
			else:
				return_value = EncryptedPatient._deserialize(result_info.success)
				return return_value

		async def undelete_patients_async(self, ids: List[IdWithMandatoryRev]) -> List[EncryptedPatient]:
			def do_decode(raw_result):
				return [EncryptedPatient._deserialize(x1) for x1 in raw_result]
			payload = {
				"ids": [x0.__serialize__() for x0 in ids],
			}
			return await execute_async_method_job(
				self.cardinal_sdk._executor,
				True,
				do_decode,
				symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.encrypted.undeletePatientsAsync,
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)

		def undelete_patients_blocking(self, ids: List[IdWithMandatoryRev]) -> List[EncryptedPatient]:
			payload = {
				"ids": [x0.__serialize__() for x0 in ids],
			}
			call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.encrypted.undeletePatientsBlocking(
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)
			result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
			symbols.DisposeString(call_result)
			if result_info.failure is not None:
				raise interpret_kt_error(result_info.failure)
			else:
				return_value = [EncryptedPatient._deserialize(x1) for x1 in result_info.success]
				return return_value

		async def get_patient_async(self, entity_id: str) -> EncryptedPatient:
			def do_decode(raw_result):
				return EncryptedPatient._deserialize(raw_result)
			payload = {
				"entityId": entity_id,
			}
			return await execute_async_method_job(
				self.cardinal_sdk._executor,
				True,
				do_decode,
				symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.encrypted.getPatientAsync,
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)

		def get_patient_blocking(self, entity_id: str) -> EncryptedPatient:
			payload = {
				"entityId": entity_id,
			}
			call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.encrypted.getPatientBlocking(
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)
			result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
			symbols.DisposeString(call_result)
			if result_info.failure is not None:
				raise interpret_kt_error(result_info.failure)
			else:
				return_value = EncryptedPatient._deserialize(result_info.success)
				return return_value

		async def get_patient_resolving_merges_async(self, patient_id: str, max_merge_depth: Optional[int]) -> EncryptedPatient:
			def do_decode(raw_result):
				return EncryptedPatient._deserialize(raw_result)
			payload = {
				"patientId": patient_id,
				"maxMergeDepth": max_merge_depth,
			}
			return await execute_async_method_job(
				self.cardinal_sdk._executor,
				True,
				do_decode,
				symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.encrypted.getPatientResolvingMergesAsync,
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)

		def get_patient_resolving_merges_blocking(self, patient_id: str, max_merge_depth: Optional[int]) -> EncryptedPatient:
			payload = {
				"patientId": patient_id,
				"maxMergeDepth": max_merge_depth,
			}
			call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.encrypted.getPatientResolvingMergesBlocking(
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)
			result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
			symbols.DisposeString(call_result)
			if result_info.failure is not None:
				raise interpret_kt_error(result_info.failure)
			else:
				return_value = EncryptedPatient._deserialize(result_info.success)
				return return_value

		async def get_patients_async(self, patient_ids: List[str]) -> List[EncryptedPatient]:
			def do_decode(raw_result):
				return [EncryptedPatient._deserialize(x1) for x1 in raw_result]
			payload = {
				"patientIds": [x0 for x0 in patient_ids],
			}
			return await execute_async_method_job(
				self.cardinal_sdk._executor,
				True,
				do_decode,
				symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.encrypted.getPatientsAsync,
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)

		def get_patients_blocking(self, patient_ids: List[str]) -> List[EncryptedPatient]:
			payload = {
				"patientIds": [x0 for x0 in patient_ids],
			}
			call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.encrypted.getPatientsBlocking(
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)
			result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
			symbols.DisposeString(call_result)
			if result_info.failure is not None:
				raise interpret_kt_error(result_info.failure)
			else:
				return_value = [EncryptedPatient._deserialize(x1) for x1 in result_info.success]
				return return_value

		async def modify_patients_async(self, patient_dtos: List[EncryptedPatient]) -> List[IdWithRev]:
			def do_decode(raw_result):
				return [IdWithRev._deserialize(x1) for x1 in raw_result]
			payload = {
				"patientDtos": [x0.__serialize__() for x0 in patient_dtos],
			}
			return await execute_async_method_job(
				self.cardinal_sdk._executor,
				True,
				do_decode,
				symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.encrypted.modifyPatientsAsync,
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)

		def modify_patients_blocking(self, patient_dtos: List[EncryptedPatient]) -> List[IdWithRev]:
			payload = {
				"patientDtos": [x0.__serialize__() for x0 in patient_dtos],
			}
			call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.encrypted.modifyPatientsBlocking(
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)
			result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
			symbols.DisposeString(call_result)
			if result_info.failure is not None:
				raise interpret_kt_error(result_info.failure)
			else:
				return_value = [IdWithRev._deserialize(x1) for x1 in result_info.success]
				return return_value

		async def merge_patients_async(self, from_: Patient, merged_into: EncryptedPatient) -> EncryptedPatient:
			def do_decode(raw_result):
				return EncryptedPatient._deserialize(raw_result)
			payload = {
				"from": serialize_patient(from_),
				"mergedInto": merged_into.__serialize__(),
			}
			return await execute_async_method_job(
				self.cardinal_sdk._executor,
				True,
				do_decode,
				symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.encrypted.mergePatientsAsync,
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)

		def merge_patients_blocking(self, from_: Patient, merged_into: EncryptedPatient) -> EncryptedPatient:
			payload = {
				"from": serialize_patient(from_),
				"mergedInto": merged_into.__serialize__(),
			}
			call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.encrypted.mergePatientsBlocking(
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)
			result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
			symbols.DisposeString(call_result)
			if result_info.failure is not None:
				raise interpret_kt_error(result_info.failure)
			else:
				return_value = EncryptedPatient._deserialize(result_info.success)
				return return_value

	class PatientFlavouredApi:

		def __init__(self, cardinal_sdk):
			self.cardinal_sdk = cardinal_sdk

		async def share_with_async(self, delegate_id: str, patient: Patient, options: Optional[PatientShareOptions] = None) -> Patient:
			def do_decode(raw_result):
				return deserialize_patient(raw_result)
			payload = {
				"delegateId": delegate_id,
				"patient": serialize_patient(patient),
				"options": options.__serialize__() if options is not None else None,
			}
			return await execute_async_method_job(
				self.cardinal_sdk._executor,
				True,
				do_decode,
				symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.tryAndRecover.shareWithAsync,
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)

		def share_with_blocking(self, delegate_id: str, patient: Patient, options: Optional[PatientShareOptions] = None) -> Patient:
			payload = {
				"delegateId": delegate_id,
				"patient": serialize_patient(patient),
				"options": options.__serialize__() if options is not None else None,
			}
			call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.tryAndRecover.shareWithBlocking(
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)
			result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
			symbols.DisposeString(call_result)
			if result_info.failure is not None:
				raise interpret_kt_error(result_info.failure)
			else:
				return_value = deserialize_patient(result_info.success)
				return return_value

		async def share_with_many_async(self, patient: Patient, delegates: Dict[str, PatientShareOptions]) -> Patient:
			def do_decode(raw_result):
				return deserialize_patient(raw_result)
			payload = {
				"patient": serialize_patient(patient),
				"delegates": {k0: v0.__serialize__() for k0, v0 in delegates.items()},
			}
			return await execute_async_method_job(
				self.cardinal_sdk._executor,
				True,
				do_decode,
				symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.tryAndRecover.shareWithManyAsync,
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)

		def share_with_many_blocking(self, patient: Patient, delegates: Dict[str, PatientShareOptions]) -> Patient:
			payload = {
				"patient": serialize_patient(patient),
				"delegates": {k0: v0.__serialize__() for k0, v0 in delegates.items()},
			}
			call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.tryAndRecover.shareWithManyBlocking(
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)
			result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
			symbols.DisposeString(call_result)
			if result_info.failure is not None:
				raise interpret_kt_error(result_info.failure)
			else:
				return_value = deserialize_patient(result_info.success)
				return return_value

		async def initialize_confidential_secret_id_async(self, patient: Patient) -> Patient:
			def do_decode(raw_result):
				return deserialize_patient(raw_result)
			payload = {
				"patient": serialize_patient(patient),
			}
			return await execute_async_method_job(
				self.cardinal_sdk._executor,
				True,
				do_decode,
				symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.tryAndRecover.initializeConfidentialSecretIdAsync,
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)

		def initialize_confidential_secret_id_blocking(self, patient: Patient) -> Patient:
			payload = {
				"patient": serialize_patient(patient),
			}
			call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.tryAndRecover.initializeConfidentialSecretIdBlocking(
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)
			result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
			symbols.DisposeString(call_result)
			if result_info.failure is not None:
				raise interpret_kt_error(result_info.failure)
			else:
				return_value = deserialize_patient(result_info.success)
				return return_value

		async def filter_patients_by_async(self, filter: FilterOptions[Patient]) -> PaginatedListIterator[Patient]:
			def do_decode(raw_result):
				return PaginatedListIterator[Patient](
					producer = raw_result,
					deserializer = lambda x: deserialize_patient(x),
					executor = self.cardinal_sdk._executor
				)
			payload = {
				"filter": filter.__serialize__(),
			}
			return await execute_async_method_job(
				self.cardinal_sdk._executor,
				False,
				do_decode,
				symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.tryAndRecover.filterPatientsByAsync,
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)

		def filter_patients_by_blocking(self, filter: FilterOptions[Patient]) -> PaginatedListIterator[Patient]:
			payload = {
				"filter": filter.__serialize__(),
			}
			call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.tryAndRecover.filterPatientsByBlocking(
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
				return PaginatedListIterator[Patient](
					producer = class_pointer,
					deserializer = lambda x: deserialize_patient(x),
					executor = self.cardinal_sdk._executor
				)

		async def filter_patients_by_sorted_async(self, filter: SortableFilterOptions[Patient]) -> PaginatedListIterator[Patient]:
			def do_decode(raw_result):
				return PaginatedListIterator[Patient](
					producer = raw_result,
					deserializer = lambda x: deserialize_patient(x),
					executor = self.cardinal_sdk._executor
				)
			payload = {
				"filter": filter.__serialize__(),
			}
			return await execute_async_method_job(
				self.cardinal_sdk._executor,
				False,
				do_decode,
				symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.tryAndRecover.filterPatientsBySortedAsync,
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)

		def filter_patients_by_sorted_blocking(self, filter: SortableFilterOptions[Patient]) -> PaginatedListIterator[Patient]:
			payload = {
				"filter": filter.__serialize__(),
			}
			call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.tryAndRecover.filterPatientsBySortedBlocking(
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
				return PaginatedListIterator[Patient](
					producer = class_pointer,
					deserializer = lambda x: deserialize_patient(x),
					executor = self.cardinal_sdk._executor
				)

		async def undelete_patient_async(self, patient: Patient) -> Patient:
			def do_decode(raw_result):
				return deserialize_patient(raw_result)
			payload = {
				"patient": serialize_patient(patient),
			}
			return await execute_async_method_job(
				self.cardinal_sdk._executor,
				True,
				do_decode,
				symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.tryAndRecover.undeletePatientAsync,
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)

		def undelete_patient_blocking(self, patient: Patient) -> Patient:
			payload = {
				"patient": serialize_patient(patient),
			}
			call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.tryAndRecover.undeletePatientBlocking(
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)
			result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
			symbols.DisposeString(call_result)
			if result_info.failure is not None:
				raise interpret_kt_error(result_info.failure)
			else:
				return_value = deserialize_patient(result_info.success)
				return return_value

		async def modify_patient_async(self, entity: Patient) -> Patient:
			def do_decode(raw_result):
				return deserialize_patient(raw_result)
			payload = {
				"entity": serialize_patient(entity),
			}
			return await execute_async_method_job(
				self.cardinal_sdk._executor,
				True,
				do_decode,
				symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.tryAndRecover.modifyPatientAsync,
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)

		def modify_patient_blocking(self, entity: Patient) -> Patient:
			payload = {
				"entity": serialize_patient(entity),
			}
			call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.tryAndRecover.modifyPatientBlocking(
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)
			result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
			symbols.DisposeString(call_result)
			if result_info.failure is not None:
				raise interpret_kt_error(result_info.failure)
			else:
				return_value = deserialize_patient(result_info.success)
				return return_value

		async def undelete_patient_by_id_async(self, id: str, rev: str) -> Patient:
			def do_decode(raw_result):
				return deserialize_patient(raw_result)
			payload = {
				"id": id,
				"rev": rev,
			}
			return await execute_async_method_job(
				self.cardinal_sdk._executor,
				True,
				do_decode,
				symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.tryAndRecover.undeletePatientByIdAsync,
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)

		def undelete_patient_by_id_blocking(self, id: str, rev: str) -> Patient:
			payload = {
				"id": id,
				"rev": rev,
			}
			call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.tryAndRecover.undeletePatientByIdBlocking(
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)
			result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
			symbols.DisposeString(call_result)
			if result_info.failure is not None:
				raise interpret_kt_error(result_info.failure)
			else:
				return_value = deserialize_patient(result_info.success)
				return return_value

		async def undelete_patients_async(self, ids: List[IdWithMandatoryRev]) -> List[Patient]:
			def do_decode(raw_result):
				return [deserialize_patient(x1) for x1 in raw_result]
			payload = {
				"ids": [x0.__serialize__() for x0 in ids],
			}
			return await execute_async_method_job(
				self.cardinal_sdk._executor,
				True,
				do_decode,
				symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.tryAndRecover.undeletePatientsAsync,
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)

		def undelete_patients_blocking(self, ids: List[IdWithMandatoryRev]) -> List[Patient]:
			payload = {
				"ids": [x0.__serialize__() for x0 in ids],
			}
			call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.tryAndRecover.undeletePatientsBlocking(
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)
			result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
			symbols.DisposeString(call_result)
			if result_info.failure is not None:
				raise interpret_kt_error(result_info.failure)
			else:
				return_value = [deserialize_patient(x1) for x1 in result_info.success]
				return return_value

		async def get_patient_async(self, entity_id: str) -> Patient:
			def do_decode(raw_result):
				return deserialize_patient(raw_result)
			payload = {
				"entityId": entity_id,
			}
			return await execute_async_method_job(
				self.cardinal_sdk._executor,
				True,
				do_decode,
				symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.tryAndRecover.getPatientAsync,
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)

		def get_patient_blocking(self, entity_id: str) -> Patient:
			payload = {
				"entityId": entity_id,
			}
			call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.tryAndRecover.getPatientBlocking(
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)
			result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
			symbols.DisposeString(call_result)
			if result_info.failure is not None:
				raise interpret_kt_error(result_info.failure)
			else:
				return_value = deserialize_patient(result_info.success)
				return return_value

		async def get_patient_resolving_merges_async(self, patient_id: str, max_merge_depth: Optional[int]) -> Patient:
			def do_decode(raw_result):
				return deserialize_patient(raw_result)
			payload = {
				"patientId": patient_id,
				"maxMergeDepth": max_merge_depth,
			}
			return await execute_async_method_job(
				self.cardinal_sdk._executor,
				True,
				do_decode,
				symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.tryAndRecover.getPatientResolvingMergesAsync,
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)

		def get_patient_resolving_merges_blocking(self, patient_id: str, max_merge_depth: Optional[int]) -> Patient:
			payload = {
				"patientId": patient_id,
				"maxMergeDepth": max_merge_depth,
			}
			call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.tryAndRecover.getPatientResolvingMergesBlocking(
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)
			result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
			symbols.DisposeString(call_result)
			if result_info.failure is not None:
				raise interpret_kt_error(result_info.failure)
			else:
				return_value = deserialize_patient(result_info.success)
				return return_value

		async def get_patients_async(self, patient_ids: List[str]) -> List[Patient]:
			def do_decode(raw_result):
				return [deserialize_patient(x1) for x1 in raw_result]
			payload = {
				"patientIds": [x0 for x0 in patient_ids],
			}
			return await execute_async_method_job(
				self.cardinal_sdk._executor,
				True,
				do_decode,
				symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.tryAndRecover.getPatientsAsync,
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)

		def get_patients_blocking(self, patient_ids: List[str]) -> List[Patient]:
			payload = {
				"patientIds": [x0 for x0 in patient_ids],
			}
			call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.tryAndRecover.getPatientsBlocking(
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)
			result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
			symbols.DisposeString(call_result)
			if result_info.failure is not None:
				raise interpret_kt_error(result_info.failure)
			else:
				return_value = [deserialize_patient(x1) for x1 in result_info.success]
				return return_value

		async def modify_patients_async(self, patient_dtos: List[EncryptedPatient]) -> List[IdWithRev]:
			def do_decode(raw_result):
				return [IdWithRev._deserialize(x1) for x1 in raw_result]
			payload = {
				"patientDtos": [x0.__serialize__() for x0 in patient_dtos],
			}
			return await execute_async_method_job(
				self.cardinal_sdk._executor,
				True,
				do_decode,
				symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.tryAndRecover.modifyPatientsAsync,
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)

		def modify_patients_blocking(self, patient_dtos: List[EncryptedPatient]) -> List[IdWithRev]:
			payload = {
				"patientDtos": [x0.__serialize__() for x0 in patient_dtos],
			}
			call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.tryAndRecover.modifyPatientsBlocking(
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)
			result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
			symbols.DisposeString(call_result)
			if result_info.failure is not None:
				raise interpret_kt_error(result_info.failure)
			else:
				return_value = [IdWithRev._deserialize(x1) for x1 in result_info.success]
				return return_value

		async def merge_patients_async(self, from_: Patient, merged_into: Patient) -> Patient:
			def do_decode(raw_result):
				return deserialize_patient(raw_result)
			payload = {
				"from": serialize_patient(from_),
				"mergedInto": serialize_patient(merged_into),
			}
			return await execute_async_method_job(
				self.cardinal_sdk._executor,
				True,
				do_decode,
				symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.tryAndRecover.mergePatientsAsync,
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)

		def merge_patients_blocking(self, from_: Patient, merged_into: Patient) -> Patient:
			payload = {
				"from": serialize_patient(from_),
				"mergedInto": serialize_patient(merged_into),
			}
			call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.tryAndRecover.mergePatientsBlocking(
				self.cardinal_sdk._native,
				json.dumps(payload).encode('utf-8'),
			)
			result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
			symbols.DisposeString(call_result)
			if result_info.failure is not None:
				raise interpret_kt_error(result_info.failure)
			else:
				return_value = deserialize_patient(result_info.success)
				return return_value

	def __init__(self, cardinal_sdk):
		self.cardinal_sdk = cardinal_sdk
		self.encrypted = PatientApi.PatientFlavouredEncryptedApi(self.cardinal_sdk)
		self.try_and_recover = PatientApi.PatientFlavouredApi(self.cardinal_sdk)

	async def get_secret_ids_of_async(self, patient: Patient) -> List[str]:
		def do_decode(raw_result):
			return [x1 for x1 in raw_result]
		payload = {
			"patient": serialize_patient(patient),
		}
		return await execute_async_method_job(
			self.cardinal_sdk._executor,
			True,
			do_decode,
			symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.getSecretIdsOfAsync,
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)

	def get_secret_ids_of_blocking(self, patient: Patient) -> List[str]:
		payload = {
			"patient": serialize_patient(patient),
		}
		call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.getSecretIdsOfBlocking(
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

	async def get_encryption_keys_of_async(self, patient: Patient) -> List[HexString]:
		def do_decode(raw_result):
			return [x1 for x1 in raw_result]
		payload = {
			"patient": serialize_patient(patient),
		}
		return await execute_async_method_job(
			self.cardinal_sdk._executor,
			True,
			do_decode,
			symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.getEncryptionKeysOfAsync,
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)

	def get_encryption_keys_of_blocking(self, patient: Patient) -> List[HexString]:
		payload = {
			"patient": serialize_patient(patient),
		}
		call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.getEncryptionKeysOfBlocking(
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

	async def create_patient_async(self, patient: DecryptedPatient) -> DecryptedPatient:
		def do_decode(raw_result):
			return DecryptedPatient._deserialize(raw_result)
		payload = {
			"patient": patient.__serialize__(),
		}
		return await execute_async_method_job(
			self.cardinal_sdk._executor,
			True,
			do_decode,
			symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.createPatientAsync,
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)

	def create_patient_blocking(self, patient: DecryptedPatient) -> DecryptedPatient:
		payload = {
			"patient": patient.__serialize__(),
		}
		call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.createPatientBlocking(
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)
		result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
		symbols.DisposeString(call_result)
		if result_info.failure is not None:
			raise interpret_kt_error(result_info.failure)
		else:
			return_value = DecryptedPatient._deserialize(result_info.success)
			return return_value

	async def with_encryption_metadata_async(self, base: Optional[DecryptedPatient], user: Optional[User] = None, delegates: Dict[str, AccessLevel] = {}) -> DecryptedPatient:
		def do_decode(raw_result):
			return DecryptedPatient._deserialize(raw_result)
		payload = {
			"base": base.__serialize__() if base is not None else None,
			"user": user.__serialize__() if user is not None else None,
			"delegates": {k0: v0.__serialize__() for k0, v0 in delegates.items()},
		}
		return await execute_async_method_job(
			self.cardinal_sdk._executor,
			True,
			do_decode,
			symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.withEncryptionMetadataAsync,
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)

	def with_encryption_metadata_blocking(self, base: Optional[DecryptedPatient], user: Optional[User] = None, delegates: Dict[str, AccessLevel] = {}) -> DecryptedPatient:
		payload = {
			"base": base.__serialize__() if base is not None else None,
			"user": user.__serialize__() if user is not None else None,
			"delegates": {k0: v0.__serialize__() for k0, v0 in delegates.items()},
		}
		call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.withEncryptionMetadataBlocking(
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)
		result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
		symbols.DisposeString(call_result)
		if result_info.failure is not None:
			raise interpret_kt_error(result_info.failure)
		else:
			return_value = DecryptedPatient._deserialize(result_info.success)
			return return_value

	async def has_write_access_async(self, patient: Patient) -> bool:
		def do_decode(raw_result):
			return raw_result
		payload = {
			"patient": serialize_patient(patient),
		}
		return await execute_async_method_job(
			self.cardinal_sdk._executor,
			True,
			do_decode,
			symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.hasWriteAccessAsync,
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)

	def has_write_access_blocking(self, patient: Patient) -> bool:
		payload = {
			"patient": serialize_patient(patient),
		}
		call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.hasWriteAccessBlocking(
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

	async def create_delegation_de_anonymization_metadata_async(self, entity: Patient, delegates: List[str]) -> None:
		def do_decode(raw_result):
			return raw_result
		payload = {
			"entity": serialize_patient(entity),
			"delegates": [x0 for x0 in delegates],
		}
		return await execute_async_method_job(
			self.cardinal_sdk._executor,
			True,
			do_decode,
			symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.createDelegationDeAnonymizationMetadataAsync,
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)

	def create_delegation_de_anonymization_metadata_blocking(self, entity: Patient, delegates: List[str]) -> None:
		payload = {
			"entity": serialize_patient(entity),
			"delegates": [x0 for x0 in delegates],
		}
		call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.createDelegationDeAnonymizationMetadataBlocking(
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)
		result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
		symbols.DisposeString(call_result)
		if result_info.failure is not None:
			raise interpret_kt_error(result_info.failure)

	async def decrypt_async(self, patient: EncryptedPatient) -> DecryptedPatient:
		def do_decode(raw_result):
			return DecryptedPatient._deserialize(raw_result)
		payload = {
			"patient": patient.__serialize__(),
		}
		return await execute_async_method_job(
			self.cardinal_sdk._executor,
			True,
			do_decode,
			symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.decryptAsync,
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)

	def decrypt_blocking(self, patient: EncryptedPatient) -> DecryptedPatient:
		payload = {
			"patient": patient.__serialize__(),
		}
		call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.decryptBlocking(
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)
		result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
		symbols.DisposeString(call_result)
		if result_info.failure is not None:
			raise interpret_kt_error(result_info.failure)
		else:
			return_value = DecryptedPatient._deserialize(result_info.success)
			return return_value

	async def try_decrypt_async(self, patient: EncryptedPatient) -> Patient:
		def do_decode(raw_result):
			return deserialize_patient(raw_result)
		payload = {
			"patient": patient.__serialize__(),
		}
		return await execute_async_method_job(
			self.cardinal_sdk._executor,
			True,
			do_decode,
			symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.tryDecryptAsync,
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)

	def try_decrypt_blocking(self, patient: EncryptedPatient) -> Patient:
		payload = {
			"patient": patient.__serialize__(),
		}
		call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.tryDecryptBlocking(
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)
		result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
		symbols.DisposeString(call_result)
		if result_info.failure is not None:
			raise interpret_kt_error(result_info.failure)
		else:
			return_value = deserialize_patient(result_info.success)
			return return_value

	async def create_patients_async(self, patient_dtos: List[DecryptedPatient]) -> List[IdWithRev]:
		def do_decode(raw_result):
			return [IdWithRev._deserialize(x1) for x1 in raw_result]
		payload = {
			"patientDtos": [x0.__serialize__() for x0 in patient_dtos],
		}
		return await execute_async_method_job(
			self.cardinal_sdk._executor,
			True,
			do_decode,
			symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.createPatientsAsync,
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)

	def create_patients_blocking(self, patient_dtos: List[DecryptedPatient]) -> List[IdWithRev]:
		payload = {
			"patientDtos": [x0.__serialize__() for x0 in patient_dtos],
		}
		call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.createPatientsBlocking(
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)
		result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
		symbols.DisposeString(call_result)
		if result_info.failure is not None:
			raise interpret_kt_error(result_info.failure)
		else:
			return_value = [IdWithRev._deserialize(x1) for x1 in result_info.success]
			return return_value

	async def share_all_data_of_patient_async(self, patient_id: str, delegates_with_share_type: Dict[str, List[ShareAllPatientDataOptions.Tag]]) -> ShareAllPatientDataOptions.Result:
		def do_decode(raw_result):
			return ShareAllPatientDataOptions.Result._deserialize(raw_result)
		payload = {
			"patientId": patient_id,
			"delegatesWithShareType": {k0: [x1.__serialize__() for x1 in v0] for k0, v0 in delegates_with_share_type.items()},
		}
		return await execute_async_method_job(
			self.cardinal_sdk._executor,
			True,
			do_decode,
			symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.shareAllDataOfPatientAsync,
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)

	def share_all_data_of_patient_blocking(self, patient_id: str, delegates_with_share_type: Dict[str, List[ShareAllPatientDataOptions.Tag]]) -> ShareAllPatientDataOptions.Result:
		payload = {
			"patientId": patient_id,
			"delegatesWithShareType": {k0: [x1.__serialize__() for x1 in v0] for k0, v0 in delegates_with_share_type.items()},
		}
		call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.shareAllDataOfPatientBlocking(
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)
		result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
		symbols.DisposeString(call_result)
		if result_info.failure is not None:
			raise interpret_kt_error(result_info.failure)
		else:
			return_value = ShareAllPatientDataOptions.Result._deserialize(result_info.success)
			return return_value

	async def get_confidential_secret_ids_of_async(self, patient: Patient) -> List[str]:
		def do_decode(raw_result):
			return [x1 for x1 in raw_result]
		payload = {
			"patient": serialize_patient(patient),
		}
		return await execute_async_method_job(
			self.cardinal_sdk._executor,
			True,
			do_decode,
			symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.getConfidentialSecretIdsOfAsync,
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)

	def get_confidential_secret_ids_of_blocking(self, patient: Patient) -> List[str]:
		payload = {
			"patient": serialize_patient(patient),
		}
		call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.getConfidentialSecretIdsOfBlocking(
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

	async def force_initialize_exchange_data_to_newly_invited_patient_async(self, patient_id: str) -> bool:
		def do_decode(raw_result):
			return raw_result
		payload = {
			"patientId": patient_id,
		}
		return await execute_async_method_job(
			self.cardinal_sdk._executor,
			True,
			do_decode,
			symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.forceInitializeExchangeDataToNewlyInvitedPatientAsync,
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)

	def force_initialize_exchange_data_to_newly_invited_patient_blocking(self, patient_id: str) -> bool:
		payload = {
			"patientId": patient_id,
		}
		call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.forceInitializeExchangeDataToNewlyInvitedPatientBlocking(
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

	async def match_patients_by_async(self, filter: FilterOptions[Patient]) -> List[str]:
		def do_decode(raw_result):
			return [x1 for x1 in raw_result]
		payload = {
			"filter": filter.__serialize__(),
		}
		return await execute_async_method_job(
			self.cardinal_sdk._executor,
			True,
			do_decode,
			symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.matchPatientsByAsync,
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)

	def match_patients_by_blocking(self, filter: FilterOptions[Patient]) -> List[str]:
		payload = {
			"filter": filter.__serialize__(),
		}
		call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.matchPatientsByBlocking(
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

	async def match_patients_by_sorted_async(self, filter: SortableFilterOptions[Patient]) -> List[str]:
		def do_decode(raw_result):
			return [x1 for x1 in raw_result]
		payload = {
			"filter": filter.__serialize__(),
		}
		return await execute_async_method_job(
			self.cardinal_sdk._executor,
			True,
			do_decode,
			symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.matchPatientsBySortedAsync,
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)

	def match_patients_by_sorted_blocking(self, filter: SortableFilterOptions[Patient]) -> List[str]:
		payload = {
			"filter": filter.__serialize__(),
		}
		call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.matchPatientsBySortedBlocking(
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

	async def ensure_encryption_metadata_for_self_is_initialized_async(self, sharing_with: Dict[str, AccessLevel] = {}) -> EncryptedPatient:
		def do_decode(raw_result):
			return EncryptedPatient._deserialize(raw_result)
		payload = {
			"sharingWith": {k0: v0.__serialize__() for k0, v0 in sharing_with.items()},
		}
		return await execute_async_method_job(
			self.cardinal_sdk._executor,
			True,
			do_decode,
			symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.ensureEncryptionMetadataForSelfIsInitializedAsync,
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)

	def ensure_encryption_metadata_for_self_is_initialized_blocking(self, sharing_with: Dict[str, AccessLevel] = {}) -> EncryptedPatient:
		payload = {
			"sharingWith": {k0: v0.__serialize__() for k0, v0 in sharing_with.items()},
		}
		call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.ensureEncryptionMetadataForSelfIsInitializedBlocking(
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)
		result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
		symbols.DisposeString(call_result)
		if result_info.failure is not None:
			raise interpret_kt_error(result_info.failure)
		else:
			return_value = EncryptedPatient._deserialize(result_info.success)
			return return_value

	async def delete_patient_by_id_async(self, entity_id: str, rev: str) -> DocIdentifier:
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
			symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.deletePatientByIdAsync,
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)

	def delete_patient_by_id_blocking(self, entity_id: str, rev: str) -> DocIdentifier:
		payload = {
			"entityId": entity_id,
			"rev": rev,
		}
		call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.deletePatientByIdBlocking(
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

	async def delete_patients_by_ids_async(self, entity_ids: List[IdWithMandatoryRev]) -> List[DocIdentifier]:
		def do_decode(raw_result):
			return [DocIdentifier._deserialize(x1) for x1 in raw_result]
		payload = {
			"entityIds": [x0.__serialize__() for x0 in entity_ids],
		}
		return await execute_async_method_job(
			self.cardinal_sdk._executor,
			True,
			do_decode,
			symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.deletePatientsByIdsAsync,
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)

	def delete_patients_by_ids_blocking(self, entity_ids: List[IdWithMandatoryRev]) -> List[DocIdentifier]:
		payload = {
			"entityIds": [x0.__serialize__() for x0 in entity_ids],
		}
		call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.deletePatientsByIdsBlocking(
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

	async def purge_patient_by_id_async(self, id: str, rev: str) -> None:
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
			symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.purgePatientByIdAsync,
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)

	def purge_patient_by_id_blocking(self, id: str, rev: str) -> None:
		payload = {
			"id": id,
			"rev": rev,
		}
		call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.purgePatientByIdBlocking(
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)
		result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
		symbols.DisposeString(call_result)
		if result_info.failure is not None:
			raise interpret_kt_error(result_info.failure)

	async def delete_patient_async(self, patient: Patient) -> DocIdentifier:
		def do_decode(raw_result):
			return DocIdentifier._deserialize(raw_result)
		payload = {
			"patient": serialize_patient(patient),
		}
		return await execute_async_method_job(
			self.cardinal_sdk._executor,
			True,
			do_decode,
			symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.deletePatientAsync,
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)

	def delete_patient_blocking(self, patient: Patient) -> DocIdentifier:
		payload = {
			"patient": serialize_patient(patient),
		}
		call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.deletePatientBlocking(
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

	async def delete_patients_async(self, patients: List[Patient]) -> List[DocIdentifier]:
		def do_decode(raw_result):
			return [DocIdentifier._deserialize(x1) for x1 in raw_result]
		payload = {
			"patients": [serialize_patient(x0) for x0 in patients],
		}
		return await execute_async_method_job(
			self.cardinal_sdk._executor,
			True,
			do_decode,
			symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.deletePatientsAsync,
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)

	def delete_patients_blocking(self, patients: List[Patient]) -> List[DocIdentifier]:
		payload = {
			"patients": [serialize_patient(x0) for x0 in patients],
		}
		call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.deletePatientsBlocking(
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

	async def purge_patient_async(self, patient: Patient) -> None:
		def do_decode(raw_result):
			return raw_result
		payload = {
			"patient": serialize_patient(patient),
		}
		return await execute_async_method_job(
			self.cardinal_sdk._executor,
			True,
			do_decode,
			symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.purgePatientAsync,
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)

	def purge_patient_blocking(self, patient: Patient) -> None:
		payload = {
			"patient": serialize_patient(patient),
		}
		call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.purgePatientBlocking(
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)
		result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
		symbols.DisposeString(call_result)
		if result_info.failure is not None:
			raise interpret_kt_error(result_info.failure)

	async def get_data_owners_with_access_to_async(self, patient: Patient) -> EntityAccessInformation:
		def do_decode(raw_result):
			return EntityAccessInformation._deserialize(raw_result)
		payload = {
			"patient": serialize_patient(patient),
		}
		return await execute_async_method_job(
			self.cardinal_sdk._executor,
			True,
			do_decode,
			symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.getDataOwnersWithAccessToAsync,
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)

	def get_data_owners_with_access_to_blocking(self, patient: Patient) -> EntityAccessInformation:
		payload = {
			"patient": serialize_patient(patient),
		}
		call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.getDataOwnersWithAccessToBlocking(
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)
		result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
		symbols.DisposeString(call_result)
		if result_info.failure is not None:
			raise interpret_kt_error(result_info.failure)
		else:
			return_value = EntityAccessInformation._deserialize(result_info.success)
			return return_value

	async def share_with_async(self, delegate_id: str, patient: DecryptedPatient, options: Optional[PatientShareOptions] = None) -> DecryptedPatient:
		def do_decode(raw_result):
			return DecryptedPatient._deserialize(raw_result)
		payload = {
			"delegateId": delegate_id,
			"patient": patient.__serialize__(),
			"options": options.__serialize__() if options is not None else None,
		}
		return await execute_async_method_job(
			self.cardinal_sdk._executor,
			True,
			do_decode,
			symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.shareWithAsync,
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)

	def share_with_blocking(self, delegate_id: str, patient: DecryptedPatient, options: Optional[PatientShareOptions] = None) -> DecryptedPatient:
		payload = {
			"delegateId": delegate_id,
			"patient": patient.__serialize__(),
			"options": options.__serialize__() if options is not None else None,
		}
		call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.shareWithBlocking(
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)
		result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
		symbols.DisposeString(call_result)
		if result_info.failure is not None:
			raise interpret_kt_error(result_info.failure)
		else:
			return_value = DecryptedPatient._deserialize(result_info.success)
			return return_value

	async def share_with_many_async(self, patient: DecryptedPatient, delegates: Dict[str, PatientShareOptions]) -> DecryptedPatient:
		def do_decode(raw_result):
			return DecryptedPatient._deserialize(raw_result)
		payload = {
			"patient": patient.__serialize__(),
			"delegates": {k0: v0.__serialize__() for k0, v0 in delegates.items()},
		}
		return await execute_async_method_job(
			self.cardinal_sdk._executor,
			True,
			do_decode,
			symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.shareWithManyAsync,
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)

	def share_with_many_blocking(self, patient: DecryptedPatient, delegates: Dict[str, PatientShareOptions]) -> DecryptedPatient:
		payload = {
			"patient": patient.__serialize__(),
			"delegates": {k0: v0.__serialize__() for k0, v0 in delegates.items()},
		}
		call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.shareWithManyBlocking(
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)
		result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
		symbols.DisposeString(call_result)
		if result_info.failure is not None:
			raise interpret_kt_error(result_info.failure)
		else:
			return_value = DecryptedPatient._deserialize(result_info.success)
			return return_value

	async def initialize_confidential_secret_id_async(self, patient: DecryptedPatient) -> DecryptedPatient:
		def do_decode(raw_result):
			return DecryptedPatient._deserialize(raw_result)
		payload = {
			"patient": patient.__serialize__(),
		}
		return await execute_async_method_job(
			self.cardinal_sdk._executor,
			True,
			do_decode,
			symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.initializeConfidentialSecretIdAsync,
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)

	def initialize_confidential_secret_id_blocking(self, patient: DecryptedPatient) -> DecryptedPatient:
		payload = {
			"patient": patient.__serialize__(),
		}
		call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.initializeConfidentialSecretIdBlocking(
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)
		result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
		symbols.DisposeString(call_result)
		if result_info.failure is not None:
			raise interpret_kt_error(result_info.failure)
		else:
			return_value = DecryptedPatient._deserialize(result_info.success)
			return return_value

	async def filter_patients_by_async(self, filter: FilterOptions[Patient]) -> PaginatedListIterator[DecryptedPatient]:
		def do_decode(raw_result):
			return PaginatedListIterator[DecryptedPatient](
				producer = raw_result,
				deserializer = lambda x: DecryptedPatient._deserialize(x),
				executor = self.cardinal_sdk._executor
			)
		payload = {
			"filter": filter.__serialize__(),
		}
		return await execute_async_method_job(
			self.cardinal_sdk._executor,
			False,
			do_decode,
			symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.filterPatientsByAsync,
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)

	def filter_patients_by_blocking(self, filter: FilterOptions[Patient]) -> PaginatedListIterator[DecryptedPatient]:
		payload = {
			"filter": filter.__serialize__(),
		}
		call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.filterPatientsByBlocking(
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
			return PaginatedListIterator[DecryptedPatient](
				producer = class_pointer,
				deserializer = lambda x: DecryptedPatient._deserialize(x),
				executor = self.cardinal_sdk._executor
			)

	async def filter_patients_by_sorted_async(self, filter: SortableFilterOptions[Patient]) -> PaginatedListIterator[DecryptedPatient]:
		def do_decode(raw_result):
			return PaginatedListIterator[DecryptedPatient](
				producer = raw_result,
				deserializer = lambda x: DecryptedPatient._deserialize(x),
				executor = self.cardinal_sdk._executor
			)
		payload = {
			"filter": filter.__serialize__(),
		}
		return await execute_async_method_job(
			self.cardinal_sdk._executor,
			False,
			do_decode,
			symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.filterPatientsBySortedAsync,
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)

	def filter_patients_by_sorted_blocking(self, filter: SortableFilterOptions[Patient]) -> PaginatedListIterator[DecryptedPatient]:
		payload = {
			"filter": filter.__serialize__(),
		}
		call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.filterPatientsBySortedBlocking(
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
			return PaginatedListIterator[DecryptedPatient](
				producer = class_pointer,
				deserializer = lambda x: DecryptedPatient._deserialize(x),
				executor = self.cardinal_sdk._executor
			)

	async def undelete_patient_async(self, patient: Patient) -> Patient:
		def do_decode(raw_result):
			return deserialize_patient(raw_result)
		payload = {
			"patient": serialize_patient(patient),
		}
		return await execute_async_method_job(
			self.cardinal_sdk._executor,
			True,
			do_decode,
			symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.undeletePatientAsync,
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)

	def undelete_patient_blocking(self, patient: Patient) -> Patient:
		payload = {
			"patient": serialize_patient(patient),
		}
		call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.undeletePatientBlocking(
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)
		result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
		symbols.DisposeString(call_result)
		if result_info.failure is not None:
			raise interpret_kt_error(result_info.failure)
		else:
			return_value = deserialize_patient(result_info.success)
			return return_value

	async def modify_patient_async(self, entity: DecryptedPatient) -> DecryptedPatient:
		def do_decode(raw_result):
			return DecryptedPatient._deserialize(raw_result)
		payload = {
			"entity": entity.__serialize__(),
		}
		return await execute_async_method_job(
			self.cardinal_sdk._executor,
			True,
			do_decode,
			symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.modifyPatientAsync,
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)

	def modify_patient_blocking(self, entity: DecryptedPatient) -> DecryptedPatient:
		payload = {
			"entity": entity.__serialize__(),
		}
		call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.modifyPatientBlocking(
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)
		result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
		symbols.DisposeString(call_result)
		if result_info.failure is not None:
			raise interpret_kt_error(result_info.failure)
		else:
			return_value = DecryptedPatient._deserialize(result_info.success)
			return return_value

	async def undelete_patient_by_id_async(self, id: str, rev: str) -> DecryptedPatient:
		def do_decode(raw_result):
			return DecryptedPatient._deserialize(raw_result)
		payload = {
			"id": id,
			"rev": rev,
		}
		return await execute_async_method_job(
			self.cardinal_sdk._executor,
			True,
			do_decode,
			symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.undeletePatientByIdAsync,
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)

	def undelete_patient_by_id_blocking(self, id: str, rev: str) -> DecryptedPatient:
		payload = {
			"id": id,
			"rev": rev,
		}
		call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.undeletePatientByIdBlocking(
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)
		result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
		symbols.DisposeString(call_result)
		if result_info.failure is not None:
			raise interpret_kt_error(result_info.failure)
		else:
			return_value = DecryptedPatient._deserialize(result_info.success)
			return return_value

	async def undelete_patients_async(self, ids: List[IdWithMandatoryRev]) -> List[DecryptedPatient]:
		def do_decode(raw_result):
			return [DecryptedPatient._deserialize(x1) for x1 in raw_result]
		payload = {
			"ids": [x0.__serialize__() for x0 in ids],
		}
		return await execute_async_method_job(
			self.cardinal_sdk._executor,
			True,
			do_decode,
			symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.undeletePatientsAsync,
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)

	def undelete_patients_blocking(self, ids: List[IdWithMandatoryRev]) -> List[DecryptedPatient]:
		payload = {
			"ids": [x0.__serialize__() for x0 in ids],
		}
		call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.undeletePatientsBlocking(
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)
		result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
		symbols.DisposeString(call_result)
		if result_info.failure is not None:
			raise interpret_kt_error(result_info.failure)
		else:
			return_value = [DecryptedPatient._deserialize(x1) for x1 in result_info.success]
			return return_value

	async def get_patient_async(self, entity_id: str) -> DecryptedPatient:
		def do_decode(raw_result):
			return DecryptedPatient._deserialize(raw_result)
		payload = {
			"entityId": entity_id,
		}
		return await execute_async_method_job(
			self.cardinal_sdk._executor,
			True,
			do_decode,
			symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.getPatientAsync,
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)

	def get_patient_blocking(self, entity_id: str) -> DecryptedPatient:
		payload = {
			"entityId": entity_id,
		}
		call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.getPatientBlocking(
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)
		result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
		symbols.DisposeString(call_result)
		if result_info.failure is not None:
			raise interpret_kt_error(result_info.failure)
		else:
			return_value = DecryptedPatient._deserialize(result_info.success)
			return return_value

	async def get_patient_resolving_merges_async(self, patient_id: str, max_merge_depth: Optional[int]) -> DecryptedPatient:
		def do_decode(raw_result):
			return DecryptedPatient._deserialize(raw_result)
		payload = {
			"patientId": patient_id,
			"maxMergeDepth": max_merge_depth,
		}
		return await execute_async_method_job(
			self.cardinal_sdk._executor,
			True,
			do_decode,
			symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.getPatientResolvingMergesAsync,
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)

	def get_patient_resolving_merges_blocking(self, patient_id: str, max_merge_depth: Optional[int]) -> DecryptedPatient:
		payload = {
			"patientId": patient_id,
			"maxMergeDepth": max_merge_depth,
		}
		call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.getPatientResolvingMergesBlocking(
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)
		result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
		symbols.DisposeString(call_result)
		if result_info.failure is not None:
			raise interpret_kt_error(result_info.failure)
		else:
			return_value = DecryptedPatient._deserialize(result_info.success)
			return return_value

	async def get_patients_async(self, patient_ids: List[str]) -> List[DecryptedPatient]:
		def do_decode(raw_result):
			return [DecryptedPatient._deserialize(x1) for x1 in raw_result]
		payload = {
			"patientIds": [x0 for x0 in patient_ids],
		}
		return await execute_async_method_job(
			self.cardinal_sdk._executor,
			True,
			do_decode,
			symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.getPatientsAsync,
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)

	def get_patients_blocking(self, patient_ids: List[str]) -> List[DecryptedPatient]:
		payload = {
			"patientIds": [x0 for x0 in patient_ids],
		}
		call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.getPatientsBlocking(
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)
		result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
		symbols.DisposeString(call_result)
		if result_info.failure is not None:
			raise interpret_kt_error(result_info.failure)
		else:
			return_value = [DecryptedPatient._deserialize(x1) for x1 in result_info.success]
			return return_value

	async def modify_patients_async(self, patient_dtos: List[EncryptedPatient]) -> List[IdWithRev]:
		def do_decode(raw_result):
			return [IdWithRev._deserialize(x1) for x1 in raw_result]
		payload = {
			"patientDtos": [x0.__serialize__() for x0 in patient_dtos],
		}
		return await execute_async_method_job(
			self.cardinal_sdk._executor,
			True,
			do_decode,
			symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.modifyPatientsAsync,
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)

	def modify_patients_blocking(self, patient_dtos: List[EncryptedPatient]) -> List[IdWithRev]:
		payload = {
			"patientDtos": [x0.__serialize__() for x0 in patient_dtos],
		}
		call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.modifyPatientsBlocking(
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)
		result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
		symbols.DisposeString(call_result)
		if result_info.failure is not None:
			raise interpret_kt_error(result_info.failure)
		else:
			return_value = [IdWithRev._deserialize(x1) for x1 in result_info.success]
			return return_value

	async def merge_patients_async(self, from_: Patient, merged_into: DecryptedPatient) -> DecryptedPatient:
		def do_decode(raw_result):
			return DecryptedPatient._deserialize(raw_result)
		payload = {
			"from": serialize_patient(from_),
			"mergedInto": merged_into.__serialize__(),
		}
		return await execute_async_method_job(
			self.cardinal_sdk._executor,
			True,
			do_decode,
			symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.mergePatientsAsync,
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)

	def merge_patients_blocking(self, from_: Patient, merged_into: DecryptedPatient) -> DecryptedPatient:
		payload = {
			"from": serialize_patient(from_),
			"mergedInto": merged_into.__serialize__(),
		}
		call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.mergePatientsBlocking(
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)
		result_info = create_result_from_json(cast(call_result, c_char_p).value.decode('utf-8'))
		symbols.DisposeString(call_result)
		if result_info.failure is not None:
			raise interpret_kt_error(result_info.failure)
		else:
			return_value = DecryptedPatient._deserialize(result_info.success)
			return return_value

	async def subscribe_to_events_async(self, events: List[SubscriptionEventType], filter: FilterOptions[Patient], subscription_config: Optional[EntitySubscriptionConfiguration] = None) -> EntitySubscription[EncryptedPatient]:
		def do_decode(raw_result):
			return EntitySubscription[EncryptedPatient](
				producer = raw_result,
				deserializer = lambda x: EncryptedPatient._deserialize(x),
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
			symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.subscribeToEventsAsync,
			self.cardinal_sdk._native,
			json.dumps(payload).encode('utf-8'),
		)

	def subscribe_to_events_blocking(self, events: List[SubscriptionEventType], filter: FilterOptions[Patient], subscription_config: Optional[EntitySubscriptionConfiguration] = None) -> EntitySubscription[EncryptedPatient]:
		payload = {
			"events": [x0.__serialize__() for x0 in events],
			"filter": filter.__serialize__(),
			"subscriptionConfig": subscription_config.__serialize__() if subscription_config is not None else None,
		}
		call_result = symbols.kotlin.root.com.icure.cardinal.sdk.py.api.PatientApi.subscribeToEventsBlocking(
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
			return EntitySubscription[EncryptedPatient](
				producer = class_pointer,
				deserializer = lambda x: EncryptedPatient._deserialize(x),
				executor = self.cardinal_sdk._executor
			)
