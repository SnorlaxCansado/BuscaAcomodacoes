// src/components/Layout.jsx
import React from 'react';
import Footer from './Footer';

const Layout = ({ children }) => {
  return (
    <div className="flex flex-col min-h-screen w-full">
      <main className="flex-grow w-full px-4 py-6">
        {children}
      </main>
      <Footer />
    </div>
  );
};

export default Layout;
