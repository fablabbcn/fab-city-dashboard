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
import os

from .scripts.app_vars import static_dir  # custom static directory

app = Flask(__name__)  # default call
# app = Flask(__name__, static_path = static_dir )
# change static directory adress to custom for Flask

from app import views
