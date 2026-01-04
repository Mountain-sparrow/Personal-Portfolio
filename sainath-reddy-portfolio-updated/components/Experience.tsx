import React from 'react';
import { Section } from './Section';
import { GlassCard } from './GlassCard';
import { EXPERIENCES } from '../constants';
import { Calendar, Briefcase } from 'lucide-react';

export const Experience: React.FC = () => {
  return (
    <Section id="experience">
      <div className="text-center mb-16">
        <h2 className="text-3xl md:text-5xl font-bold mb-4">Professional Journey</h2>
        <div className="w-24 h-1 bg-gradient-to-r from-cyan-500 to-purple-500 mx-auto rounded-full" />
      </div>

      <div className="relative max-w-4xl mx-auto">
        {/* Timeline Line */}
        <div className="absolute left-0 md:left-1/2 transform md:-translate-x-1/2 top-0 bottom-0 w-1 bg-white/10 rounded-full" />

        <div className="space-y-12">
          {EXPERIENCES.map((exp, idx) => (
            <div key={idx} className={`relative flex flex-col md:flex-row gap-8 ${idx % 2 === 0 ? 'md:flex-row-reverse' : ''}`}>
              
              {/* Timeline Dot */}
              <div className="absolute left-0 md:left-1/2 transform -translate-x-1/2 w-4 h-4 rounded-full bg-cyan-500 border-4 border-[#0A1628] z-10 mt-6 md:mt-8 shadow-[0_0_15px_rgba(6,182,212,0.8)]" />

              {/* Content Side */}
              <div className="flex-1 ml-8 md:ml-0">
                <GlassCard className="relative overflow-hidden group">
                  <div className="absolute top-0 left-0 w-1 h-full bg-gradient-to-b from-cyan-500 to-purple-600 opacity-50" />
                  
                  <div className="flex flex-col md:flex-row md:items-center justify-between mb-4 gap-2">
                    <h3 className="text-xl font-bold text-white group-hover:text-cyan-400 transition-colors">
                      {exp.role}
                    </h3>
                    <div className="flex items-center text-sm text-slate-400 bg-white/5 px-3 py-1 rounded-full w-fit">
                      <Calendar size={14} className="mr-2" />
                      {exp.period}
                    </div>
                  </div>
                  
                  <div className="flex items-center text-purple-300 text-sm font-medium mb-4">
                    <Briefcase size={16} className="mr-2" />
                    {exp.company}
                  </div>

                  <ul className="space-y-2">
                    {exp.description.map((desc, dIdx) => (
                      <li key={dIdx} className="text-slate-300 text-sm flex items-start">
                        <span className="w-1.5 h-1.5 rounded-full bg-cyan-500/50 mt-1.5 mr-3 flex-shrink-0" />
                        {desc}
                      </li>
                    ))}
                  </ul>
                </GlassCard>
              </div>

              {/* Empty Side for Layout Balance */}
              <div className="hidden md:block flex-1" />
            </div>
          ))}
        </div>
      </div>
    </Section>
  );
};