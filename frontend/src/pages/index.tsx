import { useState } from 'react';

export default function Home() {
  const [tags, setTags] = useState<string[]>([]);
  const [file, setFile] = useState<File | null>(null);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!file) return;
    const formData = new FormData();
    formData.append('image', file);

    const res = await fetch(`${process.env.NEXT_PUBLIC_API_BASE_URL}/generate_tags`, {
      method: 'POST',
      body: formData,
    });
    const data = await res.json();
    setTags(data.tags);
  };

  return (
    <div className="p-5 space-y-4">
      <h1 className="text-2xl font-bold">Gemini Tag Generator</h1>
      <form onSubmit={handleSubmit} className="space-y-2">
        <input
          type="file"
          accept="image/*"
          onChange={e => setFile(e.target.files?.[0] || null)}
          className="block"
        />
        <button type="submit" className="px-4 py-2 bg-blue-500 text-white rounded">
          Generate Tags
        </button>
      </form>
      <ul className="list-disc pl-5">
        {tags.map(t => (
          <li key={t}>{t}</li>
        ))}
      </ul>
    </div>
  );
}
