import React from 'react';
import { Section } from './Section';
import { GlassCard } from './GlassCard';
import { SOCIAL_LINKS } from '../constants';
import { Mail, Phone, MapPin, Send } from 'lucide-react';

export const Contact: React.FC = () => {
  return (
    <Section id="contact">
      <div className="text-center mb-16">
        <h2 className="text-3xl md:text-5xl font-bold mb-4">Get In Touch</h2>
        <div className="w-24 h-1 bg-gradient-to-r from-cyan-500 to-purple-500 mx-auto rounded-full" />
      </div>

      <div className="max-w-6xl mx-auto grid md:grid-cols-2 gap-12">
        {/* Contact Info */}
        <div className="space-y-8">
          <div>
            <h3 className="text-3xl font-bold mb-4 bg-clip-text text-transparent bg-gradient-to-r from-white to-slate-400">Let's Connect</h3>
            <p className="text-slate-400 leading-relaxed">
              I'm always open to discussing new opportunities, financial strategies, or just having a chat about the global economy.
            </p>
          </div>

          <div className="space-y-6">
            <GlassCard className="flex items-center gap-4 hover:bg-white/10 cursor-pointer group">
              <div className="w-12 h-12 rounded-full bg-cyan-500/20 flex items-center justify-center text-cyan-400 group-hover:scale-110 transition-transform">
                <Mail size={20} />
              </div>
              <div>
                <p className="text-sm text-slate-400">Email Me</p>
                <a href={`mailto:${SOCIAL_LINKS.email}`} className="text-white font-medium hover:text-cyan-400 transition-colors">
                  {SOCIAL_LINKS.email}
                </a>
              </div>
            </GlassCard>

            <GlassCard className="flex items-center gap-4 hover:bg-white/10 cursor-pointer group">
              <div className="w-12 h-12 rounded-full bg-purple-500/20 flex items-center justify-center text-purple-400 group-hover:scale-110 transition-transform">
                <Phone size={20} />
              </div>
              <div>
                <p className="text-sm text-slate-400">Call Me</p>
                <a href={`tel:${SOCIAL_LINKS.phone}`} className="text-white font-medium hover:text-purple-400 transition-colors">
                  {SOCIAL_LINKS.phone}
                </a>
              </div>
            </GlassCard>

            <GlassCard className="flex items-center gap-4 hover:bg-white/10 cursor-pointer group">
              <div className="w-12 h-12 rounded-full bg-pink-500/20 flex items-center justify-center text-pink-400 group-hover:scale-110 transition-transform">
                <MapPin size={20} />
              </div>
              <div>
                <p className="text-sm text-slate-400">Location</p>
                <p className="text-white font-medium">
                  {SOCIAL_LINKS.location}
                </p>
              </div>
            </GlassCard>
          </div>
        </div>

        {/* Contact Form */}
        <GlassCard>
          <form className="space-y-6" onSubmit={(e) => e.preventDefault()}>
            <div className="grid grid-cols-2 gap-6">
              <div className="col-span-2 sm:col-span-1">
                <label className="block text-sm font-medium text-slate-400 mb-2">Name</label>
                <input 
                  type="text" 
                  className="w-full bg-black/20 border border-white/10 rounded-lg px-4 py-3 text-white focus:outline-none focus:border-cyan-500 transition-colors"
                  placeholder="John Doe"
                />
              </div>
              <div className="col-span-2 sm:col-span-1">
                <label className="block text-sm font-medium text-slate-400 mb-2">Email</label>
                <input 
                  type="email" 
                  className="w-full bg-black/20 border border-white/10 rounded-lg px-4 py-3 text-white focus:outline-none focus:border-cyan-500 transition-colors"
                  placeholder="john@example.com"
                />
              </div>
            </div>
            
            <div>
              <label className="block text-sm font-medium text-slate-400 mb-2">Message</label>
              <textarea 
                rows={4}
                className="w-full bg-black/20 border border-white/10 rounded-lg px-4 py-3 text-white focus:outline-none focus:border-cyan-500 transition-colors resize-none"
                placeholder="Your message here..."
              ></textarea>
            </div>

            <button 
              className="w-full py-4 bg-gradient-to-r from-cyan-600 to-purple-600 hover:from-cyan-500 hover:to-purple-500 text-white font-bold rounded-lg shadow-lg shadow-purple-900/30 transition-all hover:scale-[1.02] flex items-center justify-center gap-2"
            >
              <Send size={18} />
              Send Message
            </button>
          </form>
        </GlassCard>
      </div>
    </Section>
  );
};