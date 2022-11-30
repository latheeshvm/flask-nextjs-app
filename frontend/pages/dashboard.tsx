import Image from "next/image";
import React, { useEffect, useRef, useState } from "react";

export default function Dashboard() {
  const [selectedFile, setSelectedFile] = useState<File[] | null>(null);
  const [preview, setPreview] = useState<string[] | []>([]);

  const handleFileSelected = (e: React.ChangeEvent<HTMLInputElement>): void => {
    const files = Array.from(e.target.files!);
    if (files != null) {
      setSelectedFile(files);
    }
  };

  useEffect(() => {
    if (selectedFile == null) {
      setPreview([]);
      return;
    }
    var data: string[] = [];
    selectedFile.forEach((item) => {
      const objectUrl = URL.createObjectURL(item);
      data.push(objectUrl);
      return () => URL.revokeObjectURL(objectUrl);
    });

    setPreview(data);
  }, [selectedFile]);

  return (
    <>
      <div className="container mx-auto flex items-center justify-center w-full p-20 flex-col">
        <label
          htmlFor="dropzone-file"
          className="flex flex-col items-center justify-center w-full h-64 border-2 border-gray-300 border-dashed rounded-lg cursor-pointer bg-gray-50 dark:hover:bg-bray-800 dark:bg-gray-700 hover:bg-gray-100 dark:border-gray-600 dark:hover:border-gray-500 dark:hover:bg-gray-600"
        >
          <div className="flex flex-col items-center justify-center pt-5 pb-6">
            <svg
              aria-hidden="true"
              className="w-10 h-10 mb-3 text-gray-400"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth="2"
                d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12"
              ></path>
            </svg>
            <p className="mb-2 text-sm text-gray-500 dark:text-gray-400">
              <span className="font-semibold">Click to upload</span> or drag and
              drop
            </p>
            <p className="text-xs text-gray-500 dark:text-gray-400">
              SVG, PNG, JPG or GIF (MAX. 800x400px)
            </p>
          </div>
          <input
            multiple
            onChange={handleFileSelected}
            id="dropzone-file"
            type="file"
            className="hidden"
          />
        </label>

        {preview.length != 0 ? (
          <div className="flex gap-20 bg-slate-400 w-full p-10 mt-7 rounded">
            {preview.map(function (item, index) {
              return (
                <>
                  <div
                    className="h-80 bg-slate-900 w-60"
                    style={{
                      backgroundImage: `url(${item})`,
                      backgroundSize: "cover",
                      backgroundPosition: "center",
                    }}
                  >
                    <></>
                  </div>
                </>
              );
            })}
          </div>
        ) : (
          <></>
        )}
        <div>
          <button className="text-white mt-20 bg-gradient-to-br from-purple-600 to-blue-500 hover:bg-gradient-to-bl focus:ring-4 focus:outline-none focus:ring-blue-300 dark:focus:ring-blue-800 font-medium rounded-lg text-sm px-5 py-2.5 text-center mr-2 mb-2">
            Compress
          </button>
        </div>
      </div>
    </>
  );
}
