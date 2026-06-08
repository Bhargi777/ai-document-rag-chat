import Link from 'next/link';

export default function HomePage() {
  return (
    <main className="min-h-screen bg-slate-950 text-slate-100 px-6 py-12">
      <div className="mx-auto max-w-5xl">
        <section className="rounded-3xl border border-slate-800 bg-slate-900/90 p-10 shadow-[0_24px_60px_rgba(15,23,42,0.25)]">
          <h1 className="text-4xl font-semibold">Document Search Chat</h1>
          <p className="mt-4 max-w-2xl text-slate-300 leading-7">
            Upload PDF documents, create searchable embeddings, and ask questions with retrieval-powered search.
          </p>
          <div className="mt-8 flex flex-col gap-4 sm:flex-row">
            <Link href="/dashboard" className="rounded-full bg-slate-700 px-6 py-3 text-sm font-semibold text-slate-100 transition hover:bg-slate-600">
              Open dashboard
            </Link>
            <Link href="/docs" className="rounded-full border border-slate-700 px-6 py-3 text-sm text-slate-200 transition hover:border-slate-500">
              Read docs
            </Link>
          </div>
        </section>
      </div>
    </main>
  );
}
