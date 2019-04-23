# formats into a pdf
# sends it as an email
class System:

    def get_data():
        pass

    def format_data(data_formatter, data):
        data_formatter.format_data(data)
        pass

    def send_data():
        pass

    def main():
        df = PDFDataFormatter()
        d = get_data()
        format_data(df, d)
        send_data()

class DataFormatter(ABC):
    @abstractmethod
    format_data(data):


    pass

class PDFDataFormatter(DataFormatter):
    pass
