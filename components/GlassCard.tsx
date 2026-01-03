import React from 'react';
import { motion } from 'framer-motion';

interface GlassCardProps {
  children: React.ReactNode;
  className?: string;
  hoverEffect?: boolean;
}

export const GlassCard: React.FC<GlassCardProps> = ({ children, className = "", hoverEffect = true }) => {
  return (
    <motion.div
      whileHover={hoverEffect ? { scale: 1.02, translateY: -5 } : {}}
      className={`glass-panel rounded-2xl p-6 md:p-8 transition-all duration-300 shadow-xl ${className}`}
    >
      {children}
    </motion.div>
  );
};