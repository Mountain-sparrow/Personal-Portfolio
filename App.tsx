import React, { useEffect, useState } from 'react';
import { Navbar } from './components/Navbar';
import { Hero } from './components/Hero';
import { About } from './components/About';
import { Skills } from './components/Skills';
import { Experience } from './components/Experience';
import { Education } from './components/Education';
import { Contact } from './components/Contact';
import { Footer } from './components/Footer';

const App: React.FC = () => {
  const [cursorPosition, setCursorPosition] = useState({ x: 0, y: 0 });

  // Ambient cursor glow effect
  useEffect(() => {
    const handleMouseMove = (e: MouseEvent) => {
      setCursorPosition({ x: e.clientX, y: e.clientY });
    };
    window.addEventListener('mousemove', handleMouseMove);
    return () => window.removeEventListener('mousemove', handleMouseMove);
  }, []);

  return (
    <div className="min-h-screen bg-[#0A1628] text-white selection:bg-cyan-500/30 selection:text-cyan-100">
      {/* Global Ambient Glow following cursor (desktop only) */}
      <div 
        className="fixed pointer-events-none inset-0 z-0 transition-opacity duration-300 hidden md:block"
        style={{
          background: `radial-gradient(600px circle at ${cursorPosition.x}px ${cursorPosition.y}px, rgba(29, 78, 216, 0.15), transparent 80%)`
        }}
      />

      <Navbar />
      
      <main className="relative z-10">
        <Hero />
        <About />
        <Skills />
        <Experience />
        <Education />
        <Contact />
      </main>

      <Footer />
    </div>
  );
};

export default App;