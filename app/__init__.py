# -*- encoding: utf-8 -*-
'''
FAB CITY DASHBOARD - VISUALIZAR'16
--------------------------------------------
A dashboard for all the Fab Cities where citizens can understand the existing resilience of cities and how the Maker movement is having an impact on this.
------------------------------------------
license: AGPL 3.0
---------------------------------------------

A project by: IAAC | Fab Lab Barcelona - Fab City Research Lab from the Fab City Global discussions.
Proposed at Visualizar'16 at Medialab Prado: http://fablabbcn.org/news/2016/05/12/visualizar.html

Participants at Visualizar'16:
    - Massimo Menichinelli (IAAC | Fab Lab Barcelona - Fab City Research Lab)
    - Mariana Quintero (IAAC | Fab Lab Barcelona - Fab City Research Lab)
    - Julien Paris (PING | LabSIC - Paris 13)
---------------------------------------------
'''

from flask import Flask

app = Flask(__name__)

from app import views

@app.route("/debug")
def debug():
    return "Hello world!"

if __name__ == "__main__":
    app.run()
