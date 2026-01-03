import React from 'react';
import { Section } from './Section';
import { GlassCard } from './GlassCard';
import { SKILL_CATEGORIES } from '../constants';
import { Code, Briefcase, User, Languages } from 'lucide-react';

const getIcon = (title: string) => {
  if (title.includes("Technical")) return <Code size={20} />;
  if (title.includes("Professional")) return <Briefcase size={20} />;
  if (title.includes("Soft")) return <User size={20} />;
  return <Languages size={20} />;
};

export const Skills: React.FC = () => {
  return (
    <Section id="skills" className="bg-[#0B182F]">
      <div className="text-center mb-16">
        <h2 className="text-3xl md:text-5xl font-bold mb-4">Skills & Expertise</h2>
        <div className="w-24 h-1 bg-gradient-to-r from-cyan-500 to-purple-500 mx-auto rounded-full" />
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        {SKILL_CATEGORIES.map((category, idx) => (
          <GlassCard key={idx} className="h-full">
            <div className="flex items-center gap-3 mb-6">
              <div className="p-2 rounded-lg bg-white/10 text-cyan-400">
                {getIcon(category.title)}
              </div>
              <h3 className="text-lg font-bold text-white">{category.title}</h3>
            </div>
            <div className="flex flex-wrap gap-2">
              {category.skills.map((skill, sIdx) => (
                <span 
                  key={sIdx}
                  className="px-3 py-1 text-sm rounded-full bg-slate-800/50 border border-slate-700 text-slate-300 hover:border-cyan-500/50 hover:text-cyan-400 transition-colors cursor-default"
                >
                  {skill}
                </span>
              ))}
            </div>
          </GlassCard>
        ))}
      </div>
    </Section>
  );
};