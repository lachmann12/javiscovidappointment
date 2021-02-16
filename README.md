# javiscovidappointment
Scans the closest COVID19 vaccination site for free appointments. It will open a new browser window and keep looking for open appoinments.

For this to work the geckodriver https://github.com/mozilla/geckodriver/releases has to be downloaded and added to the path. This is for people with preexisting conditions the software will fill in the information automatically and retry the website until it finds new appointments, it then requires additional manual input.

This is a bit buggy when the website loads too slowly it can trigger a false alarm. In that case the script needs to be restarted.
