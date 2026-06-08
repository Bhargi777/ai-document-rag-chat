import Link from 'next/link';

export default function DocsPage() {
  return (
    <main className="min-h-screen bg-slate-950 text-slate-100 px-6 py-12">
      <div className="mx-auto max-w-4xl rounded-3xl border border-slate-800 bg-slate-900/90 p-10">
        <h1 className="text-4xl font-semibold">Documentation</h1>
        <p className="mt-4 text-slate-300">
          This application supports document search, PDF ingestion, and chat over uploaded content.
        </p>
        <div className="mt-8 space-y-4 text-slate-400">
          <p>Use the dashboard to upload and manage PDFs, review indexed documents, and start chat sessions.</p>
          <p>The backend provides endpoints for auth, ingestion, retrieval, and analytics monitoring.</p>
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
