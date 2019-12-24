from pythonFuncs import correct_myfile,scan_survey,print_info,clear_survey

# +
import sys
from contextlib import contextmanager
from io import StringIO

@contextmanager
def captured_output():
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err


# -

def compare_output_with_file(func,input_file,expected_output_file):
    with captured_output() as (out,err):
        func(input_file)
        output = out.getvalue()
        with open(expected_output_file,"r") as file:
            expected_output ="".join(file.readlines())
        return output==expected_output


def compare_output_with_str(func,args,expected_string):
    with captured_output() as (out,err):
        func(*args)
        output = out.getvalue()
        return output==expected_string


# +
def test_correct_my_file():
    assert(compare_output_with_file(correct_myfile,"survey1","exp1"))
    assert(compare_output_with_file(correct_myfile,"survey2","exp_currect_survey2"))
    assert(compare_output_with_file(correct_myfile,"survey3","exp3"))
    assert(compare_output_with_file(correct_myfile,"survey4","exp4"))


    

# +
def test_print_info():
    survey = scan_survey("survey2")
    assert(compare_output_with_str(print_info,(survey,3,"Woman",30,100,"Vegan"),"[0, 0, 0, 0, 0, 0, 0, 2, 0, 0]\n"))
    assert(compare_output_with_str(print_info,(survey,3,"Woman",30,30,"Vegan"),"[0, 0, 0, 0, 0, 0, 0, 2, 0, 0]\n"))
    assert(compare_output_with_str(print_info,(survey,3,"Woman",29,30,"Vegan"),"[0, 0, 0, 0, 0, 0, 0, 2, 0, 0]\n"))
    assert(compare_output_with_str(print_info,(survey,3,"Woman",29,30,"Omnivore"),"[0, 0, 0, 0, 1, 0, 0, 0, 0, 0]\n"))
    assert(compare_output_with_str(print_info,(survey,0,"Woman",10,30,"Omnivore"),"[2, 0, 0, 0, 0, 1, 1, 0, 1, 0]\n"))
    clear_survey(survey)

    survey2 = scan_survey("survey5")
    assert(compare_output_with_str(print_info,(survey2,0,"Woman",30,31,"Omnivore"),"[4, 0, 0, 0, 0, 15, 12, 0, 0, 0]\n"))
    clear_survey(survey2)


# -

def test_clear_survey():
    ##just tests it is defined
    survey = scan_survey("survey2")
    clear_survey(survey)



if __name__=="__main__":
    print("testing correct my file")
    test_correct_my_file()
    print("testing print info")
    test_print_info()
    print("tests passed!!!!")


