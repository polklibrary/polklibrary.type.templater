# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s polklibrary.type.templater -t test_task.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src polklibrary.type.templater.testing.POLKLIBRARY_TYPE_TEMPLATER_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot src/plonetraining/testing/tests/robot/test_task.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a Task
  Given a logged-in site administrator
    and an add task form
   When I type 'My Task' into the title field
    and I submit the form
   Then a task with the title 'My Task' has been created

Scenario: As a site administrator I can view a Task
  Given a logged-in site administrator
    and a task 'My Task'
   When I go to the task view
   Then I can see the task title 'My Task'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add task form
  Go To  ${PLONE_URL}/++add++Task

a task 'My Task'
  Create content  type=Task  id=my-task  title=My Task


# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.title  ${title}

I submit the form
  Click Button  Save

I go to the task view
  Go To  ${PLONE_URL}/my-task
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a task with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the task title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
