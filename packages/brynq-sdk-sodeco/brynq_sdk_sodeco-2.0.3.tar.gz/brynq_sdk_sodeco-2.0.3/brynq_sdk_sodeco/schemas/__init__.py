"""Schema definitions for Sodeco package"""

DATEFORMAT = '%Y%m%d'

from .worker import GetWorkerSchema, PostWorkerSchema
from .absence import AbsenceSchema, AbsencesSchema
from .absencenote import AbsenceNoteSchema
from .address import AddressSchema
from .car import CarSchema
from .communication import CommunicationSchema
from .contract import ContractSchema
from .costcentre import CostCentreSchema
from .dimona import PostDimonaSchema, GetDimonaSchema, UsingDataSchema
from .divergentpayment import DivergentPaymentSchema
from .family import FamilySchema
from .replacement import ReplacementSchema
from .salarycomposition import SalaryCompositionSchema
from .schedule import ScheduleSchema
from .tax import TaxSchema
