conversation_list = """There is considerable code duplication and code similarity between the methods defined in the two classes - `BasePage` and `Raniji`.

Method Name: `click`
ClassName: `BasePage`, `Raniji`
Confidence Level: 100%
Reason: Both classes have a method named `click` which takes the same input parameters and performs the same operation on the web element.

Method Description: Waits for an element to be clickable and clicks it.
Method:
```
def click(self, locator: Tuple[By, str]) -> None:
el: WebElement = self.wait.until(expected_conditions.element_to_be_clickable(locator))
self._highlight_element(el, "green")
el.click()

def click_webelement(self, locator: Tuple[By, str]) -> None:
el: WebElement = self.wait.until(expected_conditions.element_to_be_clickable(locator))
self._highlight_element(el, ""green"")
el.click()
```

Method Name: `fill_text`
ClassName: `BasePage`, `Raniji`
Confidence Level: 100%
Reason: Both classes have a method named `fill_text` which takes the same input parameters and performs the same operation on the web element.

Method Description: Waits for an element to be clickable, clears the input field(if any), fills the input field with given `txt`
Method:
```
def fill_text(self, locator: Tuple[By, str], txt: str) -> None:
el: WebElement = self.wait.until(expected_conditions.element_to_be_clickable(locator))
el.clear()
self._highlight_element(el, "green")
el.send_keys(txt)

def fill_text(self, locator: Tuple[By, str], txt: str) -> None:
el: WebElement = self.wait.until(expected_conditions.element_to_be_clickable(locator))
el.clear()
self._highlight_element(el, ""green"")
el.send_keys(txt)
```

Method Name: `clear_text` ,   `clear_input`
ClassName: `BasePage`,  `Raniji`
Confidence Level: 67%
Reason: Both classes have a method named `clear_text` , `clear_input` are similiar as they takes the same input parameters and performs the same operation on the web element but in `clear_text`  we  are waiting for an element to be clickable.

Method Description: Waits for an element to be clickable, clears the input field(if any)
Method:
```
def clear_text(self, locator: Tuple[By, str]) -> None:
el: WebElement = self.wait.until(expected_conditions.element_to_be_clickable(locator))
el.clear()
```
Method Description: Clears the input field(if any)
Method:
```
def clear_input(self, locator: Tuple[By, str]) -> None:
el.clear()
```

Method Name: `submit`
ClassName: `BasePage`, `Raniji`
Confidence Level: 100%
Reason: Both classes have a method named `submit` which takes the same input parameters and performs the same operation on the web element.

Method Description: Submits the web element.
Method:
```
def submit(self, webelement: WebElement) -> None:
self._highlight_element(webelement, "green")
webelement.submit()

def submit_button(self, webelement: WebElement) -> None:
webelement.submit()
```

Method Name: `get_text`
ClassName: `BasePage`, `Raniji`
Confidence Level: 100%
Reason: Both classes have a method named `get_text` which takes the same input parameters and performs the same operation on the web element.

Method Description: Waits for an element to be visible and returns its text.
Method:
```
def get_text(self, locator: Tuple[By, str]) -> str:
el: WebElement = self.wait.until(expected_conditions.visibility_of_element_located(locator))
self._highlight_element(el, "green")
return el.text

def get_text(self, locator: Tuple[By, str]) -> str:
el: WebElement = self.wait.until(expected_conditions.visibility_of_element_located(locator))
self._highlight_element(el, ""green"")
return el.text
```

Method Name: `whether_elem_displayed`, `is_elem_displayed`
ClassName: `BasePage`, `Raniji`
Confidence Level: 71%
Reason: Both classes have a method named `whether_elem_displayed` , `is_elem_displayed` are similiar as they takes the same input parameters and performs the same operation on the web element but in `whether_elem_displayed` is handling StaleElementReferenceException also.

Method Description: Waits for an element to be visible and returns boolean value True or False.
Method:
```
def whether_elem_displayed(self, webelement: WebElement) -> bool:
try:
return webelement.is_displayed()
except StaleElementReferenceException:
return False
except NoSuchElementException:
return False
```

Method Description: Waits for an element to be visible and returns boolean value True or False.
Method:
```
def is_elem_displayed(self, webelement: WebElement) -> bool:
try:
return webelement.is_displayed()
except NoSuchElementException:
return False
```
"""

"""

"""
