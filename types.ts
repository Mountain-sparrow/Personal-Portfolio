export interface ExperienceItem {
  role: string;
  company: string;
  period: string;
  description: string[];
}

export interface SkillCategory {
  title: string;
  skills: string[];
}

export interface EducationItem {
  degree: string;
  institution: string;
  details: string;
}

export interface NavItem {
  label: string;
  href: string;
}