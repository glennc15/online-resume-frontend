(function() {

    angular
        .module('onlineResume')
        .service('onlineResumeData', onlineResumeData);


    onlineResumeData.$inject = ["$http"];
    function onlineResumeData($http) {


        var apiGetResumeJson = function() {

            // return $http.get('/api/locations?lng=' + lng + '&lat=' + lat + '&maxDistance=5');

            return $http.get('https://l1wd7bw8cf.execute-api.us-east-1.amazonaws.com/serverless_lambda_stage/resume');


        };


        return {
            apiGetResumeJson: apiGetResumeJson,
        };

    };


    })();



            // var data = {
            //     name: "Glenn Crosby",
            //     location: "Alvin, Texas",

            //     titleLinks: [
            //         {
            //             "icon": "fa-envelope",
            //             "link": "mailto:glenn@glenn.dev",
            //             "display": "glenn@glenn.dev",
            //         },
            //         {
            //             "icon": "fa-phone",
            //             "link": "tel:+12816944143",
            //             "display": "+1 (281) 694-4143",
            //         },
            //         {
            //             "icon": "fa-linkedin",
            //             "link": "https://www.linkedin.com/in/glenncrosby",
            //             "display": "https://www.linkedin.com/in/glenncrosby",
            //         },
            //         {
            //             "icon": "fa-github",
            //             "link": "https://github.com/glennc15",
            //             "display": "https://github.com/glennc15",
            //         },
            //     ],

            //     professionalSummary: [
            //         "Dynamic and results-oriented professional with extensive experience in project management, commissioning, and technical leadership within the oil and gas industry. Proven track record of managing diverse teams, ensuring compliance with industry standards, and maintaining exceptional client relationships. Skilled in project planning, equipment installation, commissioning, and quality assurance. Proficient in programming languages such as Python and JavaScript, with expertise in industrial networking protocols and PLC hardware. Seeking to leverage strong technical acumen, problem-solving abilities, and a commitment to excellence in a challenging data engineering role",
            //     ],

            //     leftSkills: [
            //         {
            //             heading: "Data Engineering",
            //             skills: ["Apache Airflow", "AWS", "Terraform"],
            //         },
            //         {
            //             heading: "Web Scraping",
            //             skills: ["Scrapy", "Playwright", "Requests", "Bash"],
            //         },
            //         {
            //             heading: "DevOps",
            //             skills: ["Docker", "GitHub", "CI/CD"],
            //         },
            //         {
            //             heading: "Web Development",
            //             skills: ["Angular", "HTML", "CSS"],
            //         },
            //         {
            //             heading: "Database Systems",
            //             skills: ["MongoDB", "PostgreSQL"],
            //         },
            //         {
            //             heading: "Programming Languages",
            //             skills: ["Python", "JavaScript"],
            //         },
            //         {
            //             heading: "Operating Systems",
            //             skills: ["Mac OS", "GNU/Linux", "Windows"],
            //         },
            //     ],

            //     rightSkills: [
            //         {
            //             heading: "Industrial Programming",
            //             skills: ["SCL", "STL", "Ladder Logic"],
            //         },
            //         {
            //             heading: "Industrial Networks",
            //             skills: ["Profibus DP", "Modbus", "Industrial Ethernet"],
            //         },
            //         {
            //             heading: "Industrial Hardware",
            //             skills: ["Siement 300/400H", "Allen Bradley PLC5/SLC", "Omron"],
            //         },

            //     ],

            //     experience: [
            //         {
            //             title: "Installation and Commissioning Manager",
            //             company: "National Oilwell Varco",
            //             location: "China/UAE",
            //             dates: "Jan 2010 - Sep 2019",
            //             list: false,
            //             paragraphs: [
            //                 "I oversaw complex projects related to the installation and commissioning of cutting-edge equipment in the oil and gas industry. My responsibilities included project planning, team leadership, and ensuring the successful integration of equipment in challenging operational environments, contributing to the company's reputation for excellence.",
            //             ]
            //         },
            //         {
            //             title: "Commissioning Engineer",
            //             company: "National Oilwell Varco",
            //             location: "China/Korea/Singapore/UAE",
            //             dates: "May 2000 - Jan 2010",
            //             list: false,
            //             paragraphs: [
            //                 "I specialized in overseeing the commissioning process for oil and gas equipment. My role emphasized a commitment to safety, strong troubleshooting skills, and effective communication. I thrived in remote and challenging work environments while maintaining meticulous documentation of critical processes.",
            //             ]
            //         },
            //         {
            //             title: "Electrical Designer",
            //             company: "Champion Elevators",
            //             location: "Houston, TX",
            //             dates: "May 1999 - May 2000",
            //             list: true,
            //             paragraphs: [
            //                 "Produced detailed electrical schematics and panel assembly drawings, complete with comprehensive BOMs, using AutoCAD and Solid Edge.",
            //                 "Develop custom elevator control software on Omron and Allen Bradley PLCs, along with intuitive HMI interfaces, enhancing elevator system efficiency and functionality."
            //             ]
            //         },
            //         {
            //             title: "Control Technician",
            //             company: "Tejas Boiler Service",
            //             location: "Houston, TX",
            //             dates: "Sep 1994 - May 1999",
            //             list: true,
            //             paragraphs: [
            //                 "Integral member of a dynamic engineering team, actively involved in diverse engineering disciplines.",
            //                 "Designed custom burner monitoring and boiler control software for Allen Bradley PLCs meeting stringent NFPA 8502 requirements."
            //             ]
            //         },
            //         {
            //             title: "Electrician's Mate, Second Class",
            //             company: "United States Navy",
            //             location: "USS Sturgeon",
            //             dates: "Aug 1989 - Aug 1994",
            //             list: false,
            //             paragraphs: [
            //                 "As a US Navy Nuclear-Trained Electrician on a fast attack submarine, I held a critical role in ensuring the safe and reliable operation of the ship's electrical systems, contributing to mission success and crew safety in challenging and dynamic environments.",
            //             ]
            //         },
            //     ],

            //     education: [
            //         {
            //             name: "AWS Certified Cloud Practitioner",
            //             dates: "Mar 2024",
            //         },
            //         {
            //             name: "Houston Community College @ Main Campus, Houston, TX",
            //             dates: "Jan 1995 - Jul 1998",
            //         },
            //         {
            //             name: "Naval Nuclear Power School @ NTC Orlando, Fl",
            //             dates: "Jul 1990 - Dec 1990",
            //         },
            //     ],
            //     visitors: 637,
            // };

            // return data;


