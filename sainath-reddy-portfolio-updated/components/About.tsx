import React from 'react';
import { Section } from './Section';
import { GlassCard } from './GlassCard';
import { Target, Globe, BookOpen } from 'lucide-react';

export const About: React.FC = () => {
  return (
    <Section id="about">
      <div className="text-center mb-16">
        <h2 className="text-3xl md:text-5xl font-bold mb-4">About Me</h2>
        <div className="w-24 h-1 bg-gradient-to-r from-cyan-500 to-purple-500 mx-auto rounded-full" />
      </div>

      <div className="grid md:grid-cols-3 gap-8">
        <GlassCard className="col-span-1 md:col-span-2">
          <h3 className="text-2xl font-semibold mb-6 text-cyan-400">Professional Summary</h3>
          <p className="text-slate-300 leading-relaxed text-lg mb-6">
            I am a detail-oriented financial professional with extensive experience in financial analysis, data insights, and strategic support. My background includes robust technical proficiency in SAP, Excel VBA, and RPA, allowing me to streamline workflows and enhance process efficiency.
          </p>
          <p className="text-slate-300 leading-relaxed text-lg">
            As a Lusophone professional, I possess Upper Intermediate (B2) proficiency in Portuguese, enabling me to manage cross-border operations effectively in Latin American and Iberian markets. I pride myself on strong organizational skills and collaborative problem-solving.
          </p>
        </GlassCard>

        <div className="flex flex-col gap-6">
          <GlassCard className="flex-1 flex flex-col items-center text-center justify-center">
            <div className="w-12 h-12 rounded-full bg-purple-500/20 flex items-center justify-center mb-4 text-purple-400">
              <Target size={24} />
            </div>
            <h4 className="font-semibold text-white mb-2">Goal Oriented</h4>
            <p className="text-sm text-slate-400">Pursuing CMA US (Mar 2025)</p>
          </GlassCard>
          
          <GlassCard className="flex-1 flex flex-col items-center text-center justify-center">
             <div className="w-12 h-12 rounded-full bg-cyan-500/20 flex items-center justify-center mb-4 text-cyan-400">
              <Globe size={24} />
            </div>
            <h4 className="font-semibold text-white mb-2">Multilingual</h4>
            <p className="text-sm text-slate-400">English, Portuguese, Telugu</p>
          </GlassCard>

          <GlassCard className="flex-1 flex flex-col items-center text-center justify-center">
             <div className="w-12 h-12 rounded-full bg-pink-500/20 flex items-center justify-center mb-4 text-pink-400">
              <BookOpen size={24} />
            </div>
            <h4 className="font-semibold text-white mb-2">Continuous Learner</h4>
            <p className="text-sm text-slate-400">Always upskilling in Tech & Finance</p>
          </GlassCard>
        </div>
      </div>
    </Section>
  );
};