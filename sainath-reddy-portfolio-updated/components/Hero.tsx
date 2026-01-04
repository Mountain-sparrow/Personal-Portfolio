import React from 'react';
import { motion } from 'framer-motion';
import { Mail, MapPin, Linkedin, Phone, ArrowDown } from 'lucide-react';
import { SOCIAL_LINKS } from '../constants';

export const Hero: React.FC = () => {
  return (
    <section className="min-h-screen flex items-center justify-center relative overflow-hidden pt-20">
      {/* Background Ambience */}
      <div className="absolute top-0 left-1/4 w-96 h-96 bg-purple-600/20 rounded-full blur-[128px] pointer-events-none" />
      <div className="absolute bottom-0 right-1/4 w-96 h-96 bg-cyan-600/20 rounded-full blur-[128px] pointer-events-none" />

      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10 w-full">
        <div className="flex flex-col lg:flex-row items-center gap-12 lg:gap-20">
          
          {/* Text Content */}
          <motion.div 
            initial={{ opacity: 0, x: -50 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ duration: 0.8, delay: 0.2 }}
            className="flex-1 text-center lg:text-left order-2 lg:order-1"
          >
            <div className="inline-block px-4 py-2 rounded-full bg-cyan-500/10 border border-cyan-500/20 text-cyan-300 text-sm font-semibold mb-6">
              Financial Specialist & CMA Candidate
            </div>
            
            <h1 className="text-5xl lg:text-7xl font-bold mb-6 tracking-tight">
              Hello, I'm <br />
              <span className="text-gradient">Sainath Reddy</span>
            </h1>
            
            <p className="text-xl text-slate-300 mb-8 max-w-2xl mx-auto lg:mx-0 leading-relaxed">
              Multilingual Finance Professional specializing in data insights, strategic support, and process automation. 
              Currently mastering Portuguese (B2) and pursuing CMA US certification.
            </p>

            <div className="flex flex-wrap items-center justify-center lg:justify-start gap-4 mb-10">
              <a 
                href={`mailto:${SOCIAL_LINKS.email}`}
                className="flex items-center gap-2 px-4 py-2 rounded-lg bg-white/5 hover:bg-white/10 border border-white/10 transition-colors text-sm text-slate-200"
              >
                <Mail size={16} className="text-cyan-400" />
                {SOCIAL_LINKS.email}
              </a>
              <div className="flex items-center gap-2 px-4 py-2 rounded-lg bg-white/5 border border-white/10 text-sm text-slate-200">
                <MapPin size={16} className="text-purple-400" />
                Andhra Pradesh, India
              </div>
            </div>

            <div className="flex items-center justify-center lg:justify-start gap-6">
              <a 
                href={SOCIAL_LINKS.linkedin}
                target="_blank"
                rel="noopener noreferrer"
                className="flex items-center gap-3 px-8 py-4 bg-gradient-to-r from-blue-600 to-cyan-600 hover:from-blue-500 hover:to-cyan-500 text-white rounded-full font-semibold shadow-lg shadow-cyan-900/50 transition-all hover:scale-105"
              >
                <Linkedin size={20} />
                Connect on LinkedIn
              </a>
              <a 
                href="#contact"
                className="flex items-center gap-3 px-8 py-4 bg-white/5 hover:bg-white/10 border border-white/20 text-white rounded-full font-semibold transition-all hover:scale-105"
              >
                <Phone size={20} />
                Contact Me
              </a>
            </div>
          </motion.div>

          {/* Image */}
          <motion.div 
            initial={{ opacity: 0, scale: 0.8 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ duration: 0.8 }}
            className="flex-1 order-1 lg:order-2 flex justify-center lg:justify-end"
          >
            <div className="relative w-72 h-72 lg:w-96 lg:h-96">
              {/* Outer Glow Ring */}
              <div className="absolute inset-0 rounded-full bg-gradient-to-tr from-cyan-500 to-purple-600 blur-2xl opacity-50 animate-pulse" />
              
              {/* Image Container */}
              <div className="absolute inset-2 rounded-full p-2 bg-gradient-to-tr from-white/20 to-white/5 border border-white/20 backdrop-blur-sm overflow-hidden z-10">
                <img 
                  src="/assets/profile.jpg" 
                  alt="Sainath Reddy" 
                  className="w-full h-full object-cover rounded-full"
                />
              </div>

              {/* Decorative Elements */}
              <div className="absolute -top-4 -right-4 w-24 h-24 bg-white/10 backdrop-blur-md rounded-2xl border border-white/20 z-20 flex items-center justify-center animate-bounce-slow">
                <span className="text-3xl">📊</span>
              </div>
              <div className="absolute -bottom-4 -left-4 w-20 h-20 bg-white/10 backdrop-blur-md rounded-full border border-white/20 z-20 flex items-center justify-center animate-bounce-slow delay-700">
                <span className="text-2xl">🇧🇷</span>
              </div>
            </div>
          </motion.div>

        </div>

        <motion.div 
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 1, duration: 1 }}
          className="absolute bottom-10 left-1/2 transform -translate-x-1/2 animate-bounce text-slate-400"
        >
          <ArrowDown size={24} />
        </motion.div>
      </div>
    </section>
  );
};