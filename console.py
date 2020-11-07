#!/usr/bin/python3
''' Module that supports the console behavior
'''
import cmd
import sys
import json
from models.engine.file_storage import FileStorage


class idClasses:
    """Class for all other classes"""
    from models.base_model import BaseModel
    from models.user import User
    from models.engine.file_storage import FileStorage
    from models.state import State
    from models.city import City
    from models.amenity import Amenity
    from models.place import Place
    from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Class for command interpreter"""
    prompt = '(hbnb) '
    file = None

    def point_all(self, arg):
        args = arg.split(".")
        if "()" in arg and len(args) is 2:
            string = args[1].split("(")[0] + " " + args[0]
            return string
        else:
            return arg

    def point_count(self, arg):
        args = arg.split(".")
        if "()" in arg and len(args) is 2:
            string = args[1].split("(")[0] + " " + args[0]
            return string
        else:
            return arg

    def point_show(self, arg):
        args = arg.split(".")
        if "(" and ")" in arg and len(args) is 2:
            new = args[1].split("(\"")
            new[1] = new[1].split("\")")[0]
            string = new[0] + " " + args[0] + " " + new[1]
            return string
        else:
            return arg

    def point_destroy(self, arg):
        args = arg.split(".")
        if "(" and ")" in arg and len(args) is 2:
            new = args[1].split("(\"")
            new[1] = new[1].split("\")")[0]
            string = new[0] + " " + args[0] + " " + new[1]
            return string
        else:
            return arg

    def point_update(self, arg):
        args = arg.split(".")
        if "(" and ")" in arg and len(args) is 3:
            args[2] = args[2].split("(\"")[1]
            args[2] = args[2].split("\")")[0]
            args[2] = args[2].split("\", \"")
            string = args[1] + " " + args[0] + " " + args[2][0]\
                + " " + args[2][1] + " " + args[2][2]
            return string
        else:
            return arg

    def precmd(self, arg):
        x = self.point_all(arg)
        if(x == arg):
            x = self.point_count(arg)
        if(x == arg):
            x = self.point_show(arg)
        if(x == arg):
            x = self.point_destroy(arg)
        if(x == arg):
            x = self.point_update(arg)
        return x

    def do_quit(self, arg):
        "Quit command to exit the program\n"
        sys.exit(0)

    def do_EOF(self, arg):
        "Quit command to exit the program\n"
        sys.exit(0)

    def emptyline(self):
        """Ignores empty spaces"""
        pass

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel
        and saves it to JSON file
        """
        if(arg == ""):
            print("** class name missing **")
        elif(not hasattr(idClasses, arg)):
            print("** class doesn't exist **")
        else:
            targetClass = getattr(idClasses, arg)
            new = targetClass()
            new.save()
            print(new.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        f = FileStorage()
        f.reload()
        objs = f.all()
        args = arg.split()
        if(arg == ""):
            print("** class name missing **")
        elif (not hasattr(idClasses, args[0])):
            print("** class doesn't exist **")
        elif (len(args) < 2):
            print("** instance id missing **")
        else:
            obj = ['', '']
            for key in objs:
                obj = [objs[key].__class__.__name__, objs[key].id]
                if obj == args:
                    print(objs[key])
                    return
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        f = FileStorage()
        f.reload()
        objs = f.all()
        args = arg.split()
        if(arg == ""):
            print("** class name missing **")
        elif(not hasattr(idClasses, args[0])):
            print("** class doesn't exist **")
        elif (len(args) < 2):
            print("** instance id missing **")
        else:
            obj = ['', '']
            for key in objs:
                obj = [objs[key].__class__.__name__, objs[key].id]
                if obj == args:
                    del objs[key]
                    f.save()
                    return
            print("** no instance found **")

    def do_all(self, arg):
        """
        Prints the string representation of an instance
        based on the class name
        """
        f = FileStorage()
        f.reload()
        objs = f.all()
        ls = []
        if arg == "":
            for key in objs:
                ls.append(str(objs[key]))
            print(ls)
        elif(not hasattr(idClasses, arg)):
            print("** class doesn't exist **")
        else:
            for key in objs:
                cl = key.split(".")
                if cl[0] == arg:
                    ls.append(str(objs[key]))
            print(ls)

    def do_update(self, arg):
        """
        Change the argument key of an instance
        based on the class name and id
        """
        f = FileStorage()
        f.reload()
        objs = f.all()
        args = arg.split()
        if(arg == ""):
            print("** class name missing **")
        elif(not hasattr(idClasses, args[0])):
            print("** class doesn't exist **")
        elif(len(args) < 2):
            print("** instance id missing **")
        elif not(args[0]+"."+args[1] in objs):
                print("** no instance found **")
        elif (len(args) < 3):
            print("** attribute name missing **")
        elif (len(args) < 4):
            print("** value missing **")
        else:
            for key in objs:
                obj = key.split(".")
                if obj[0] == args[0] and obj[1] == args[1]:
                    value = objs[key]
                    setattr(value, args[2], args[3])
                    f.save()

    def do_count(self, arg):
        f = FileStorage()
        f.reload()
        objs = f.all()
        x = 0
        for obj in objs:
            obj = obj.split(".")
            if obj[0] == arg:
                x += 1
        print(x)

if __name__ == "__main__":
    HBNBCommand().cmdloop()
