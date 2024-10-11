from abc import ABC, abstractmethod


class CompanyReportRepository(ABC):
    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def create(self, companyReportName, companyReportPrice, companyReportCategory, content, companyReportTitleImage):
        pass

    @abstractmethod
    def update(self,companyReport,companyReportData):
        pass

    @abstractmethod
    def findByCompanyReportId(self, companyReportId):
        pass

    @abstractmethod
    def findByCompanyReportIdList(self, companyReportIdList):
        pass

    @abstractmethod
    def findAllByCompanyReportCategory(self, companyReportCategory):
        pass

    @abstractmethod
    def deleteByCompanyReportId(self,companyReportId):
        pass

    @abstractmethod
    def readCompanyReportFinance(self, companyReportName):
        pass

    @abstractmethod
    def readCompanyReportInfo(self,companyReportName):
        pass

    @abstractmethod
    def readCompanyReportSummary(self,companyReportName):
        pass