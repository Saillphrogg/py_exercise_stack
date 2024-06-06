class Stack:
    def __init__(self,data_type=None):
            self.stack=[]
            self.data_type = data_type

    def push(self,data):
        if self.data_type in None or isinstance(data, self.data_type):
            self.stack.append(data)
   
    def pop(self):
        if self.stack:
            self.stack.pop()
        else:
            return None

    def get(self):
        if self.stack:
            return self.stack[-1]
        else:
            return None   

    def length(self):
        return len(self.stack)
        

    def __repr__(self):
        return repr(self.stack)  