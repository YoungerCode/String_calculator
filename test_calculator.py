from calculator import add
import pytest

#Test case 1.1: Test an empty string
def test_add_empty_str():
    assert add("") == 0
    
#Test case 1.2: Test one number
def test_add_one_number():
    assert add("1") == 1
    
#Test case 1.3: Test two number
def test_add_two_number():
    assert add("1,10") == 11
    
#Test case 2: Test unknown amount of numbers 
def test_add_unknown_amount_of_numbers():
    assert add("1,2,3,4,5") == 15
    
#Test case 3.1: Test handling new lines
def test_add_new_lines():
    assert add("1\n2,3") == 6
    
    
#Test case 4.1: Test support different delimiters
def test_add_different_delimiters():
    assert add("//;\n1;2") == 3
  
#Test case 4.2: Test existing scenarios
def test_add_existing_scenarios():
    assert add("1;2;;1") == 4
    
#Test case 5: Test negative number will throw an exception “negatives not allowed”
def test_add_neg_num():
    with pytest.raises(Exception) as err:
        add("-1,-1,2")
    assert 'negatives not allowed' in str(err.value) 

test_add_neg_num()
  
#Test case 6: Test numbers bigger than 1000 are ignored
def test_add_bigger_numbers():
    assert add("2+1001") == 2
    
#Test case 7: Test delimiters of any length
def test_add_delimiters():
    assert add("//[***]\n1***2***3") == 6
    
#Test case 8: Test multiple delimiters of any length
def test_add_multiple_delimiters():
    assert add("//[*][%]\n1*2%3") == 6  
    
#Test case 9: Test multiple delimiters with length longer than one char    
def test_add_multiple_delimiters_longer():
    assert add("//[*][%]\n1*2%++++++@aqw^^^^^^^3") == 6
