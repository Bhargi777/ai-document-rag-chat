import { Sidebar } from '../../../components/sidebar';

export default function DocumentsPage() {
  return (
    <div className="min-h-screen bg-slate-950 text-slate-100">
      <div className="grid min-h-screen grid-cols-[280px_1fr]">
        <Sidebar />
        <main className="p-8">
          <section className="rounded-3xl border border-slate-800 bg-slate-900/90 p-8">
            <h1 className="text-3xl font-semibold">Documents</h1>
            <p className="mt-3 text-slate-400">View uploaded files, metadata, and retrieval statistics.</p>
            <div className="mt-8 grid gap-4">
              <div className="rounded-3xl border border-slate-800 bg-slate-950 p-6">No documents uploaded yet.</div>
            </div>
          </section>
        </main>
      </div>
    </div>
  );
}
