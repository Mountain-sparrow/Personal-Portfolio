import React from 'react';

export const Footer: React.FC = () => {
  return (
    <footer className="py-8 border-t border-white/5 bg-[#050B14] text-center">
      <p className="text-slate-500 text-sm">
        © {new Date().getFullYear()} Sainath Reddy. All rights reserved.
      </p>
      <div className="mt-2 text-xs text-slate-600">
        Designed with futuristic glassmorphism
      </div>
    </footer>
  );
};