import { ExperienceItem, SkillCategory, EducationItem, NavItem } from './types';

// Navigation
export const NAV_ITEMS: NavItem[] = [
  { label: 'About', href: '#about' },
  { label: 'Skills', href: '#skills' },
  { label: 'Experience', href: '#experience' },
  { label: 'Education', href: '#education' },
  { label: 'Contact', href: '#contact' },
];

// Experience Data
export const EXPERIENCES: ExperienceItem[] = [
  {
    role: "Financial Specialist",
    company: "Lennox India Technology Centre",
    period: "April 2024 - Present",
    description: [
      "Leading Utility Rebates Project with streamlined workflows",
      "Managed Sales Commissions Project transition across multiple teams",
      "Handling sales commissions: new hires, terminations, PAP configs, bonus calculations",
      "Ownership of Commercial Pricing process and reports",
      "Automated Unallocated Price Catalog updates via RPA",
      "Restructured Commodities PPI report for enhanced clarity",
      "Monitor competitor pricing via ACHR news for strategic decisions",
      "Contribute to RFPs and HVAC bids"
    ]
  },
  {
    role: "Senior Financial Analyst & Portuguese Language Expert",
    company: "Lennox India Technology Centre",
    period: "Jan 2022 - Mar 2024",
    description: [
      "Managed new start-up setups and equipment installations",
      "Created quotes and purchase orders with accuracy",
      "Processed cash applications for Spain",
      "Managed e-service and FMB operations for Portugal",
      "Provided customer documentation and technician support"
    ]
  },
  {
    role: "Portuguese Language Specialist",
    company: "Corteva Agriscience",
    period: "Jun 2020 - Feb 2022",
    description: [
      "Processed invoices for Latin America region",
      "Managed vendor accounts and refund collections",
      "Resolved ServiceNow tickets for payment queries"
    ]
  },
  {
    role: "Business Analyst (Cert Management)",
    company: "Accenture",
    period: "Nov 2018 - Jun 2020",
    description: [
      "Anchored credit collections for Brazil",
      "Client communications in Portuguese",
      "ServiceNow ticket resolution"
    ]
  },
  {
    role: "Customer Delight Executive",
    company: "Swiggy",
    period: "Apr 2018 - Nov 2018",
    description: [
      "Real-time customer query resolution",
      "Chat management with <15 second FRT",
      "Email and call support"
    ]
  }
];

// Skills Data
export const SKILL_CATEGORIES: SkillCategory[] = [
  {
    title: "Technical Skills",
    skills: ["SAP", "MS Excel VBA", "ServiceNow", "Financial Analysis", "RPA (Automation)"]
  },
  {
    title: "Professional Skills",
    skills: ["FP&A", "Sales Commissions", "Commercial Pricing", "Quote & PO Creation", "Invoice Processing", "Cash Applications", "Credit Collections"]
  },
  {
    title: "Soft Skills",
    skills: ["Quick Learning", "Effective Communication", "Client Value Creation", "Problem Solving", "Cross-functional Collaboration"]
  },
  {
    title: "Languages",
    skills: ["Telugu (Native)", "English (C1 Advanced)", "Portuguese (B2 Upper Intermediate)", "Tamil (Intermediate)"]
  }
];

// Education Data
export const EDUCATION: EducationItem[] = [
  {
    degree: "Certified Management Accountant (CMA US)",
    institution: "Institute of Management Accountants (IMA)",
    details: "Expected: March 2025 | Focus: Management Accounting and Finance"
  },
  {
    degree: "Diploma in Portuguese & English",
    institution: "RDT Professional School of Foreign Languages",
    details: "Levels: B1 Portuguese, C1 English"
  },
  {
    degree: "B.Sc. Mathematics, Statistics & Computer Science",
    institution: "Sri Krishnadevaraya University, Anantapur A.P",
    details: "Undergraduate Degree"
  }
];

export const SOCIAL_LINKS = {
  linkedin: "https://www.linkedin.com/in/sainath-reddyb32526120/",
  email: "reddysainath286@gmail.com",
  phone: "+91-9177048939",
  location: "Kothacheruvu, Andhra Pradesh 515133"
};