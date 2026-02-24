from Presentation.Desktop.view_manager import ViewManager
from Business.employee_business import EmployeeBusiness
from DataAccess.Repositories.SQLiteRepositories.employee_repository import SQLiteEmployeeRepository
from DataAccess.Repositories.SQLServerRepositories.employee_repository import SQLServerEmployeeRepository


# sqlite_employee_repository = SQLiteEmployeeRepository("CoreBankingDB.db")
sqlite_employee_repository = SQLServerEmployeeRepository('CoreBankingDB')

employee_business = EmployeeBusiness(sqlite_employee_repository)

ViewManager(employee_business)

