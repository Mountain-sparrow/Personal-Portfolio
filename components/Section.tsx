import React from 'react';
import { motion } from 'framer-motion';

interface SectionProps {
  id: string;
  children: React.ReactNode;
  className?: string;
}

export const Section: React.FC<SectionProps> = ({ id, children, className = "" }) => {
  return (
    <section id={id} className={`py-20 md:py-32 px-4 relative overflow-hidden ${className}`}>
      <motion.div
        initial={{ opacity: 0, y: 50 }}
        whileInView={{ opacity: 1, y: 0 }}
        viewport={{ once: true, margin: "-100px" }}
        transition={{ duration: 0.8, ease: "easeOut" }}
        className="max-w-6xl mx-auto relative z-10"
      >
        {children}
      </motion.div>
    </section>
  );
};