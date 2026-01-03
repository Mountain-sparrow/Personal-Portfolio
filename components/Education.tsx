import React from 'react';
import { Section } from './Section';
import { GlassCard } from './GlassCard';
import { EDUCATION } from '../constants';
import { Award, GraduationCap } from 'lucide-react';

export const Education: React.FC = () => {
  return (
    <Section id="education" className="bg-[#0B182F]">
      <div className="text-center mb-16">
        <h2 className="text-3xl md:text-5xl font-bold mb-4">Education & Certification</h2>
        <div className="w-24 h-1 bg-gradient-to-r from-cyan-500 to-purple-500 mx-auto rounded-full" />
      </div>

      <div className="grid md:grid-cols-3 gap-8">
        {EDUCATION.map((edu, idx) => (
          <GlassCard key={idx} className="flex flex-col h-full border-t-4 border-t-cyan-500">
            <div className="mb-6 w-14 h-14 rounded-2xl bg-gradient-to-br from-cyan-500/20 to-purple-600/20 flex items-center justify-center text-cyan-400">
              {idx === 0 ? <Award size={32} /> : <GraduationCap size={32} />}
            </div>
            <h3 className="text-xl font-bold text-white mb-2 h-14">{edu.degree}</h3>
            <p className="text-purple-300 font-medium mb-4">{edu.institution}</p>
            <div className="mt-auto pt-4 border-t border-white/5">
              <p className="text-slate-400 text-sm leading-relaxed">{edu.details}</p>
            </div>
          </GlassCard>
        ))}
      </div>
      
      {/* Activities Mini Section */}
      <div className="mt-20">
        <h3 className="text-2xl font-bold mb-8 text-center text-white">Activities & Interests</h3>
        <div className="grid md:grid-cols-2 gap-6 max-w-4xl mx-auto">
          <GlassCard>
            <h4 className="font-bold text-cyan-400 mb-2">Volunteering</h4>
            <ul className="space-y-2 text-slate-300 text-sm">
              <li>• Active Member: Vadaanya Jana Society (NGO)</li>
              <li>• CSR Activities: Beach clean-ups, Charity runs</li>
            </ul>
          </GlassCard>
          <GlassCard>
            <h4 className="font-bold text-purple-400 mb-2">Interests</h4>
            <ul className="space-y-2 text-slate-300 text-sm">
              <li>• Listening to Finance & Tech Podcasts</li>
              <li>• Reading Non-fiction books on Economics</li>
            </ul>
          </GlassCard>
        </div>
      </div>
    </Section>
  );
};