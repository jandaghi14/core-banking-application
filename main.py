from Presentation.Desktop.view_manager import ViewManager
from Business.employee_business import EmployeeBusiness
from DataAccess.Repositories.SQLiteRepositories.employee_repository import SQLiteEmployeeRepository


sqlite_employee_repository = SQLiteEmployeeRepository("CoreBankingDB.db")

employee_business = EmployeeBusiness(sqlite_employee_repository)

ViewManager(employee_business)

