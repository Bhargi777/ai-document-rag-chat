import Link from 'next/link';

export default function AdminPage() {
  return (
    <main className="min-h-screen bg-slate-950 text-slate-100 px-6 py-12">
      <div className="mx-auto max-w-5xl rounded-3xl border border-slate-800 bg-slate-900/90 p-10">
        <h1 className="text-4xl font-semibold">Admin Dashboard</h1>
        <p className="mt-4 text-slate-400">A supervisor interface for application health, document moderation, and user management.</p>
        <div className="mt-8 space-y-4 text-slate-300">
          <p>Admin features are planned for managing uploads, sessions, and usage analytics.</p>
        </div>
        <div className="mt-8">
          <Link href="/dashboard" className="rounded-full bg-slate-700 px-6 py-3 text-sm font-semibold text-slate-100 hover:bg-slate-600">
            Back to Dashboard
          </Link>
        </div>
      </div>
    </main>
  );
}
