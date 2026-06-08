"use client";

import React, { useState } from 'react';

export function ThemeToggle() {
  const [dark, setDark] = useState(true);

  return (
    <button
      type="button"
      onClick={() => setDark(!dark)}
      className="rounded-full border border-slate-700 bg-slate-900 px-4 py-2 text-sm text-slate-200 transition hover:bg-slate-800"
    >
      {dark ? 'Dark mode' : 'Light mode'}
    </button>
  );
}
