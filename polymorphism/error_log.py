# •	11. Create a class `Logger` with a method `log(message)`.
# Implement method overloading to log different message types (`error`, `warning`, `info`).


    # def log(self,message):
    #     print("message is: ",message)
    # def log(self,message,error):
    #     print("message or error is :",error)
    # def log(self,message,error,warning):
    #     print("waringin is:",warning)
    # def log(self,message,error,warning,info):
class Logger:
    def log(self, message, level="info"):
        level = level.lower()  
        if level == "error":
            print(f"[ERROR]: {message}")
        elif level == "warning":
            print(f"[WARNING]: {message}")
        else:
            print(f"[INFO]: {message}")

# Example usage
logger = Logger()
logger.log("System started")              
logger.log("Low disk space", "warning")   
logger.log("File not found", "error")    
