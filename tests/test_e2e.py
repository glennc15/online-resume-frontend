import pytest
import os
import re
from playwright.sync_api import Page, expect


# base_url = "http://localhost:8081"

@pytest.fixture
def config():
    config = dict()

    url = os.environ.get('URL')
    if url:
        config['URL'] = url
    else:
        config['URL'] = 'http://localhost:8081'

    return config




def test_resume_name_is_correct(page: Page, config):
    page.goto(config.get('URL'))
    expect(page.get_by_text("Glenn Crosby")).to_be_visible()


def test_location(page: Page, config):
    page.goto(config.get('URL'))
    expect(page.get_by_text("Alvin, Texas")).to_be_visible()

def test_email_link(page: Page, config):
    page.goto(config.get('URL'))
    expect(page.get_by_role("link", name="gcrosby15@gmail.com")).to_be_visible()

def test_phone_link(page: Page, config):
    page.goto(config.get('URL'))
    expect(page.get_by_role("link", name="+1 (281) 694-4143")).to_be_visible()

def test_linkedin_link(page: Page, config):
    page.goto(config.get('URL'))
    expect(page.get_by_role("link", name="in/glenncrosby")).to_be_visible()

def test_gethub_link(page: Page, config):
    page.goto(config.get('URL'))
    expect(page.get_by_role("link", name="https://github.com/glennc15")).to_be_visible()

def test_data_eng_skills(page: Page, config):
    page.goto(config.get('URL'))

    # have to use an xpath locator because "Data Engineering" is used in several
    # differenct places. Without xpath causes a strict mode error.
    expect(page.locator("xpath=//section[3]//div//div[2]//div[1]//div[1][text()='Data Engineering']")).to_be_visible()
    # expect(page.get_by_text("Data Engineering")).to_be_visible()

    expect(page.get_by_text("Apache Airflow ⸱ AWS ⸱ Terraform")).to_be_visible()

def test_web_scraping_skills(page: Page, config):
    page.goto(config.get('URL'))
    expect(page.get_by_text("Web Scraping")).to_be_visible()
    expect(page.get_by_text("Scrapy ⸱ Playwright ⸱ Requests ⸱ Bash")).to_be_visible()

def test_devops_skills(page: Page, config):
    page.goto(config.get('URL'))
    expect(page.get_by_text("DevOps")).to_be_visible()
    expect(page.get_by_text("Docker ⸱ GitHub ⸱ CI/CD")).to_be_visible()

def test_web_development_skills(page: Page, config):
    page.goto(config.get('URL'))
    expect(page.get_by_text("Web Development")).to_be_visible()
    expect(page.get_by_text("Angular ⸱ HTML ⸱ CSS")).to_be_visible()

def test_database_skills(page: Page, config):
    page.goto(config.get('URL'))
    expect(page.get_by_text("Database Systems")).to_be_visible()
    expect(page.get_by_text("MongoDB ⸱ PostgreSQL")).to_be_visible()

def test_programming_languages_skills(page: Page, config):
    page.goto(config.get('URL'))

    # have to use an xpath locator because "Programming Languages" is used in several
    # differenct places. Without xpath causes a strict mode error.
    expect(page.locator("xpath=//section[3]/div//div[3]//div[3]//div[1][text()='Programming Languages']")).to_be_visible()
    # expect(page.get_by_text("Programming Languages")).to_be_visible()

    expect(page.get_by_text("Python ⸱ JavaScript")).to_be_visible()

def test_operating_systems_skills(page: Page, config):
    page.goto(config.get('URL'))
    expect(page.get_by_text("Operating Systems")).to_be_visible()
    expect(page.get_by_text("Mac OS ⸱ GNU/Linux ⸱ Windows")).to_be_visible()

def test_industrial_programming_skills(page: Page, config):
    page.goto(config.get('URL'))
    expect(page.get_by_text("Industrial Programming")).to_be_visible()
    expect(page.get_by_text("SCL ⸱ STL ⸱ Ladder Logic")).to_be_visible()

def test_industrial_networks_skills(page: Page, config):
    page.goto(config.get('URL'))
    expect(page.get_by_text("Industrial Networks")).to_be_visible()
    expect(page.get_by_text("Profibus DP ⸱ Modbus ⸱ Industrial Ethernet")).to_be_visible()

def test_industrial_hardware_skills(page: Page, config):
    page.goto(config.get('URL'))
    expect(page.get_by_text("Industrial Hardware")).to_be_visible()
    expect(page.get_by_text("Siement 300/400H ⸱ Allen Bradley PLC5/SLC ⸱ Omron")).to_be_visible()

def test_data_engineer_experience(page: Page, config):
    page.goto(config.get('URL'))
    expect(page.get_by_text("Data Engineer @ Self-Employed")).to_be_visible()

    expect(page.locator("xpath=/html/body/div/div[2]/div/section[1]/div/div[2]/div[1]/small[text()='Houston, TX']")).to_be_visible()
    # expect(page.get_by_text("Houston, TX")).to_be_visible()

    expect(page.get_by_text("Jan 2020 - Present")).to_be_visible()
    expect(page.get_by_text("Responsible for developing and maintaining Python scripts and web scrapers for financial data extraction, processing, and storage, with a strong emphasis on Test Driven Development (TDD) methodology. Experienced in managing MongoDB databases, including building and maintaining local servers.")).to_be_visible()


def test_commissioning_manager_experience(page: Page, config):
    page.goto(config.get('URL'))
    expect(page.get_by_text("Installation and Commissioning Manager @ National Oilwell Varco")).to_be_visible()
    expect(page.get_by_text("China/UAE")).to_be_visible()
    expect(page.get_by_text("Jan 2010 - Sep 2019")).to_be_visible()
    expect(page.get_by_text("I oversaw complex projects related to the installation and commissioning of cutting-edge equipment in the oil and gas industry. My responsibilities included project planning, team leadership, and ensuring the successful integration of equipment in challenging operational environments, contributing to the company's reputation for excellence.")).to_be_visible()

def test_commissioning_engineer_experience(page: Page, config):
    page.goto(config.get('URL'))
    expect(page.get_by_text("Commissioning Engineer @ National Oilwell Varco")).to_be_visible()
    expect(page.get_by_text("China/Korea/Singapore/UAE")).to_be_visible()
    expect(page.get_by_text("May 2000 - Jan 2010")).to_be_visible()
    expect(page.get_by_text("I specialized in overseeing the commissioning process for oil and gas equipment. My role emphasized a commitment to safety, strong troubleshooting skills, and effective communication. I thrived in remote and challenging work environments while maintaining meticulous documentation of critical processes.")).to_be_visible()

def test_electrical_designer_experience(page: Page, config):
    page.goto(config.get('URL'))
    expect(page.get_by_text("Electrical Designer @ Champion Elevators")).to_be_visible()

    # /html/body/div/div[2]/div/section[1]/div/div[4]/div[1]/small
    # /html/body/div/div[2]/div/section[1]/div/div[4]/div[1]/small

    # have to use an xpath locator because "Houston, TX" is used in several
    # differenct places. Without xpath causes a strict mode error.
    expect(page.locator("xpath=//div[5]//div[1]//small[text()='Houston, TX']")).to_be_visible()
    # expect(page.get_by_text("Houston, TX")).to_be_visible()

    expect(page.get_by_text("May 1999 - May 2000")).to_be_visible()
    expect(page.get_by_text("Produced detailed electrical schematics and panel assembly drawings, complete with comprehensive BOMs, using AutoCAD and Solid Edge.")).to_be_visible()
    expect(page.get_by_text("Develop custom elevator control software on Omron and Allen Bradley PLCs, along with intuitive HMI interfaces, enhancing elevator system efficiency and functionality.")).to_be_visible()

def test_boiler_technician_experience(page: Page, config):
    page.goto(config.get('URL'))
    expect(page.get_by_text("Control Technician @ Tejas Boiler Service")).to_be_visible()

    # /html/body/div/div[2]/div/section[1]/div/div[5]/div[1]/small

    # have to use an xpath locator because "Houston, TX" is used in several
    # differenct places. Without xpath causes a strict mode error.
    expect(page.locator("xpath=//div[5]//div[1]//small[text()='Houston, TX']")).to_be_visible()
    # expect(page.get_by_text("Houston, TX")).to_be_visible()


    expect(page.get_by_text("Sep 1994 - May 1999")).to_be_visible()
    expect(page.get_by_text("Integral member of a dynamic engineering team, actively involved in diverse engineering disciplines.")).to_be_visible()
    expect(page.get_by_text("Designed custom burner monitoring and boiler control software for Allen Bradley PLCs meeting stringent NFPA 8502 requirements.")).to_be_visible()

def test_navy_experience(page: Page, config):
    page.goto(config.get('URL'))
    expect(page.get_by_text("Electrician's Mate, Second Class @ United States Navy")).to_be_visible()
    expect(page.get_by_text("USS Sturgeon")).to_be_visible()
    expect(page.get_by_text("Aug 1989 - Aug 1994")).to_be_visible()
    expect(page.get_by_text("As a US Navy Nuclear-Trained Electrician on a fast attack submarine, I held a critical role in ensuring the safe and reliable operation of the ship's electrical systems, contributing to mission success and crew safety in challenging and dynamic environments.")).to_be_visible()

def test_AWS_education(page: Page, config):
    page.goto(config.get('URL'))
    expect(page.get_by_text("AWS Certified Cloud Practitioner")).to_be_visible()
    expect(page.get_by_text("Mar 2024")).to_be_visible()

def test_HCC_education(page: Page, config):
    page.goto(config.get('URL'))
    expect(page.get_by_text("Houston Community College @ Main Campus, Houston, TX")).to_be_visible()
    expect(page.get_by_text("Jan 1995 - Jul 1998")).to_be_visible()


def test_navy_education(page: Page, config):
    page.goto(config.get('URL'))
    expect(page.get_by_text("Naval Nuclear Power School @ NTC Orlando, Fl")).to_be_visible()
    expect(page.get_by_text("Jul 1990 - Dec 1990")).to_be_visible()


def test_visitors_counter(page: Page, config):
    page.goto(config.get('URL'))
    expect(page.get_by_text("You are visitor: 0,")).to_be_visible()
