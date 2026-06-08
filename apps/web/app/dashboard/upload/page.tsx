import { Sidebar } from '../../../components/sidebar';

export default function UploadPage() {
  return (
    <div className="min-h-screen bg-slate-950 text-slate-100">
      <div className="grid min-h-screen grid-cols-[280px_1fr]">
        <Sidebar />
        <main className="p-8">
          <section className="rounded-3xl border border-slate-800 bg-slate-900/90 p-8">
            <h1 className="text-3xl font-semibold">Upload Documents</h1>
            <p className="mt-3 text-slate-400">Upload PDFs and build searchable document embeddings.</p>
            <div className="mt-8 rounded-3xl border-2 border-dashed border-slate-700 p-12 text-center">
              <p className="text-slate-500">Upload UI will connect to the document ingestion API here.</p>
            </div>
          </section>
        </main>
      </div>
    </div>
  );
}
