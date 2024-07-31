import sys
class JsonException(Exception):
    pass

class Json():
    def __init__(self,string) -> None:
        self.string=string
        self.index = 0

    def whitespace_parser(self):
        while(self.string[self.index] in [" ","\n","\t","\r"]):
            self.index += 1

    def string_parser(self):
        if (self.string[self.index]=='"'):
            self.index+=1
            try:
                while(self.string[self.index] != '"'):  
                    self.index+=1    
                self.index+=1    
            except IndexError:
                raise JsonException("Invalid JSON : missing closing quotes")
        else:
            raise JsonException("Key value pair Expected after ,")

        
    def int_parser(self):
        if self.string[self.index] == "-":
            self.index += 1

        if self.string[self.index] == "0":
            self.index += 1

        elif self.string[self.index].isnumeric():
            self.index += 1
            while self.string[self.index].isnumeric():
                self.index += 1

        if self.string[self.index] == ".":
            self.index += 1
            while self.string[self.index].isnumeric():
                self.index += 1

        if self.string[self.index].lower() == "e":
            self.index += 1
            if self.string[self.index] in ["-", "+"]:
                self.index += 1
            while self.string[self.index].isnumeric():
                self.index += 1

    def keyword_parser(self):
        if(self.string[self.index:self.index+4] == "true"):
            self.index += 4
        elif(self.string[self.index:self.index+5] == "false"):
            self.index += 5
        elif(self.string[self.index:self.index+4] == "null"):
            self.index += 4
        else:
            raise JsonException("keyword Expected")


    def colon_parser(self):
        try:
            if(self.string[self.index] == ':'):
                self.index+=1  
            else:
                print("Invalid JSON : missing colon (:)")
        except IndexError:
            print("Invalid JSON : Incomplete object")
        
    def value_parser(self):
        self.whitespace_parser()
        if(self.string[self.index] == '"'):
            self.string_parser()
        elif(self.string[self.index].isnumeric() or self.string[self.index]=='-'):
            self.int_parser()
        elif(self.string[self.index] == '{'):
            self.object_parser()
        elif(self.string[self.index] == '['):
            self.array_parser()
        elif(self.string[self.index].isalpha()):
            self.keyword_parser()
        else:
            raise JsonException("invalid value")
        
    def array_parser(self):
        if(self.string[self.index] == '['):
            self.index+=1
            self.whitespace_parser()
            if(self.string[self.index]=="]"):
                if(self.index<len(self.string)-1):
                    self.index+=1
                    return
                else:
                    print("Valid JSON")
                    sys.exit(0)
            else:
                self.value_parser()
            while(self.string[self.index]==","):
                self.value_parser()
            if(self.string[self.index] == ']'):
                self.index+=1
            else:
                raise JsonException("closing square bracket missing")


    def key_value_parser(self):
        self.string_parser()
        self.whitespace_parser()
        self.colon_parser()
        self.whitespace_parser()
        self.value_parser()
        self.whitespace_parser()

    def comma_parser(self):
        if(self.string[self.index]==","):
            self.index += 1

    def object_parser(self):
        try:
            if(self.string[self.index] == '{'):
                self.index +=1
                self.whitespace_parser()
                if(self.string[self.index] == '}'):
                    if(self.index<len(self.string)-1):
                        self.index+=1
                    else:
                        print("Valid JSON")
                        sys.exit(0)
                elif(self.string[self.index] == '"'):
                    self.key_value_parser()
                    if(self.string[self.index] == "}" and self.index<len(self.string)-1):
                        self.index+=1
                else:
                    raise JsonException("string expected")
                self.x = self.string[self.index]
                while(self.string[self.index] == ","):
                    self.comma_parser()
                    self.whitespace_parser()
                    self.key_value_parser()
                    

                self.whitespace_parser()
                if(self.string[self.index] == '}'):
                    print("Valid JSON")
                    sys.exit(0)
                else:
                    raise JsonException("closing curly bracket missing")
            elif(self.string[self.index] == '['):
                self.array_parser()
            else:
                raise JsonException("open curly bracket expected")
        except IndexError:
            raise JsonException("index error")

            

            


            






    