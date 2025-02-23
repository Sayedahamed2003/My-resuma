from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def resume():
    resume_data = {
        'name': 'Sayed Ahamed',
        'profession': 'Aspiring Cloud Engineer',
        'contact': {
            'email': 'nizarahamednsa3000@gmail.com',
            'phone': '9962260359',
            'linkedin': 'https://www.linkedin.com/in/sayedahamed',
            'github': 'https://github.com/sayedahamed'
        },
        'skills': ['Linux', 'AWS', 'Azure', 'Terraform', 'DevOps', 'Python'],
        'certifications': ['AWS Certified Solutions Architect', 'Microsoft Certified: Azure Fundamentals'],
        'expertise': ['Excel', 'PowerPoint', 'OneDrive', 'OneNote'],
        'languages': {'Tamil': '100%', 'Hindi': '100%', 'English': '67%'},
        'interests': ['Gaming', 'Music', 'Coffee'],
        'experience': [
            {
                'job_title': 'Linux, AWS, Cisco Intern',
                'company': 'Mentor Fox Pvt. Ltd.',
                'duration': 'May 2024 - Aug 2024',
                'description': [
                    'Gained hands-on experience in managing Linux-based environments, ensuring system performance and security.',
                    'Assisted in deploying and managing cloud infrastructure on AWS, optimizing resource utilization and cost efficiency.',
                    'Configured and maintained Cisco networking equipment, enhancing network reliability and security.',
                    'Collaborated with team members to automate workflows and streamline processes, improving operational efficiency.',
                    'Troubleshot and resolved technical issues, providing support to ensure smooth IT operations.'
                ]
            }
        ],
        'education': [
            {
                'degree': 'Bachelor in Information Technology',
                'institution': 'Anna University',
                'college': 'Meenakshi College of Engineering',
                'gpa': '8.3 / 10 GPA'
            }
        ]
    }
    return render_template('resume.html', resume=resume_data)

if __name__ == '__main__':
    app.run(debug=True)
