# from mymodule import my_func
# my_func()

#from MyMainPackage import some_main_script
#from MyMainPackage.SubPackage import mysubscript
from MyMainPackage.some_main_script import report_main
from MyMainPackage.SubPackage.mysubscript import sub_report

#some_main_script.report_main()
#mysubscript.sub_report()
report_main()
sub_report()
