import React from 'react';
import Link from 'next/link';
import { ThemeToggle } from './theme-toggle';

const navItems = [
  { href: '/dashboard', label: 'Dashboard' },
  { href: '/dashboard/upload', label: 'Upload' },
  { href: '/dashboard/chat', label: 'Chat' },
  { href: '/dashboard/documents', label: 'Documents' },
  { href: '/dashboard/analytics', label: 'Analytics' },
] as const;

export function Sidebar() {
  return (
    <aside className="w-72 border-r border-slate-800 bg-slate-950/95 p-6">
      <div className="mb-10 space-y-3">
        <h2 className="text-sm uppercase tracking-[0.3em] text-slate-500">Workspace</h2>
        {navItems.map((item) => (
          <Link
            key={item.href}
            href={item.href}
            className="block rounded-2xl px-4 py-3 text-sm text-slate-200 transition hover:bg-slate-900"
          >
            {item.label}
          </Link>
        ))}
      </div>
      <div className="mt-auto pt-6">
        <ThemeToggle />
      </div>
    </aside>
  );
}
