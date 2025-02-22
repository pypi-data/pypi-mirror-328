#
#	PRMI.py
#
#	(c) 2023 by Andreas Kraft
#	License: BSD 3-Clause License. See the LICENSE file for further details.
#
#	ResourceType: ProcessManagement
#

from __future__ import annotations
from typing import Optional, Any, Union

from ..resources.Resource import Resource

from ..etc.Types import AttributePolicyDict, ResourceTypes, JSON, ProcessState, ProcessControl
from ..resources.AnnounceableResource import AnnounceableResource
from ..helpers.TextTools import findXPath
from ..etc.ResponseStatusCodes import OPERATION_NOT_ALLOWED

# TODO annc version
# TODO add to UML diagram
# TODO add to statistics, also in console


class PRMR(AnnounceableResource):

	# Specify the allowed child-resource types
	_allowedChildResourceTypes = [ ResourceTypes.STTE,
							   	   ResourceTypes.SUB
								 ]
	""" The allowed child-resource types. """


	# Attributes and Attribute policies for this Resource Class
	# Assigned during startup in the Importer
	_attributes:AttributePolicyDict = {		
		# Common and universal attributes
		'rn': None,
		'ty': None,
		'ri': None,
		'pi': None,
		'ct': None,
		'lt': None,
		'et': None,
		'acpi': None,
		'lbl': None,
		'cr': None,
		'cstn': None,
		'daci': None,

		'at': None,
		'aa': None,
		'ast': None,

		# Resource attributes
		'prst': None,
		'prct': None,
		'cust': None,
		'atcos': None,
		'encos': None,
		'inst': None,
	}
	"""	Attributes and `AttributePolicy` for this resource type. """

	def __init__(self, dct:Optional[JSON] = None, 
					   pi:Optional[str] = None, 
					   create:Optional[bool] = False) -> None:
		""" Initialize the PRMR resource instance.
		
			Args:
				dct: The JSON dictionary with the resource attributes.
				pi: The parent resource ID.
				create: Create a new resource instance. Default is *False*.
		"""
		super().__init__(ResourceTypes.PRMR, dct, pi, create = create)


	def activate(self, parentResource: Resource, originator: str) -> None:
		super().activate(parentResource, originator)

		# Set the initial processStatus to Disabled
		self.setAttribute('prst', ProcessState.Disabled.value)

		# Set the initial processControl to Disable
		self.setAttribute('prct', ProcessControl.Disable.value)

		# EXPERIMENTAL: the currentState (cust) and initialState (inst) are NOT present initially

	
	def update(self, dct: JSON = None, originator: str | None = None, doValidateAttributes: bool | None = True) -> None:

		# current processState
		prst = self.prst

		# Step 1) Update of initialState, activateCondition or endCondition attributes
		newInst = findXPath(dct, 'm2m:prmr/inst')
		newAtcos = findXPath(dct, 'm2m:prmr/atcos')
		newEncos = findXPath(dct, 'm2m:prmr/encos')
		if any([newInst, newAtcos, newEncos]) and prst != ProcessState.Disabled:
			raise OPERATION_NOT_ALLOWED('Process state must be "disabled" to update the initialState, activateCondition or endCondition attributes')	

		# Step 2) Check existence and access for activateCondition and endCondition
		if newAtcos:
			# TODO check existence if and access to resources and attributes referenced by the subject element of the evalCriteria element
			# Check <action> code to reuse the code from the <action> resource
			# If not: Return error "INVALID_PROCESS_CONFIGURATION"
			pass
		if newEncos:
			# TODO check existence if and access to resources and attributes referenced by the subject element of the evalCriteria element
			# Check <action> code to reuse the code from the <action> resource
			# If not: Return error "INVALID_PROCESS_CONFIGURATION"
			pass
	

		# Step 3) Check threshold of the values and operator in the activateCondition and endCondition attributes
		if newAtcos:
			# TODO check threshold of the values and operator in the activateCondition attribute
			# Check <action> code to reuse the code from the <action> resource
			# If not: Return error "INVALID_PROCESS_CONFIGURATION"
			pass
		if newEncos:
			# TODO check threshold of the values and operator in the endCondition attribute
			# Check <action> code to reuse the code from the <action> resource
			# If not: Return error "INVALID_PROCESS_CONFIGURATION"
			pass
	
		# Step 4) Check existence and access to the <state> resource referenced by the (new) initialState attribute
		if newInst:
			# TODO check existence access to the <state> resource referenced by the (new) initialState attribute, and RETRIEVE privileges for the originator
			# If not: Return error "INVALID_PROCESS_CONFIGURATION"
			pass

		#
		# Check processControl updates
		#
		
		match (newPrct := findXPath(dct, 'm2m:prmr/prct')):
			
			# Failure
			# Step 5)
			case ProcessControl.Enable if prst != ProcessState.Disabled:
				raise OPERATION_NOT_ALLOWED('Process state must be "disabled" to enable the process')
			# Step 6)
			case ProcessControl.Disable if prst == ProcessState.Disabled:
				raise OPERATION_NOT_ALLOWED('Process state must not be "disabled" to disable the process')
			# Step 7)
			case ProcessControl.Pause if prst != ProcessState.Activated:
				raise OPERATION_NOT_ALLOWED('Process state must be "activated" to pause the process')
			# Step 8)
			case ProcessControl.Reactivate if prst != ProcessState.Paused:
				raise OPERATION_NOT_ALLOWED('Process state must be "paused" to reactivate the process')
			
			# Success
			# Step 9)
			case ProcessControl.Enable if prst == ProcessState.Disabled:

				# Does the <state> resource referenced by the initialState attribute exist?
				# Is it a child resource of this resource?
				# has the originator retrieve privileges on it?
				
				# Does the originator has proper CRUD privileges for the <state> and <action> resources referenced by this resource and child resources?
				# Are all the referenced resources child resources of this resource?
				# Are all the referenced resources of the correct resource types?

				# If yes: Set processStatus to "enabled"
				# Start the process
				# If no: Return error "INVALID_PROCESS_CONFIGURATION"
				pass
			# Step 10)
			case ProcessControl.Pause if prst == ProcessState.Activated:
				self.setAttribute('prst', ProcessState.Paused.value)
				# TODO pause the process
			
			# Step 11)
			case ProcessControl.Reactivate if prst == ProcessState.Paused:
				self.setAttribute('prst', ProcessState.Activated.value)
				# TODO continues processing the process
			
			# Step 12)
			case ProcessControl.Disable if prst != ProcessState.Disabled:
				self.setAttribute('prst', ProcessState.Disabled.value)
				self.delAttribute('cust')	# EXPERIMENTAL
				# TODO set the stateActive attribute of the current <state> resource to false
				# TODO disable the process



		super().update(dct, originator, doValidateAttributes)	


	# EXPERIMENTAL Don't define a deactivate() method. This would cause problems with deregistering of AEs