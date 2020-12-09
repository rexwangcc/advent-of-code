(ns solution1
  (:require [clojure.string :as str]))

(defn get-lines
  "Read in inputs as seq of integers."
  [file]
  (map read-string (str/split-lines (slurp file))))

(defn two-sum
  [inputs target]
  (loop [l  inputs
         seen #{}]
    (when-let [curr (first l)]
      (if (seen (- target curr))
        true
        (recur (rest l) (conj seen curr))))))


(defn slide
  "Slide through the list using a window and
   outsource the searching to 2sum."
  [inputs]
  (letfn [(get-preamble-window [coll n offset]
            (->> coll
                 (drop offset)
                 (take n)))]
    (loop [offset 0
           idx 25]
      (let [window (get-preamble-window inputs 25 offset)
            curr (nth inputs idx)]
        (if-not (two-sum window curr)
          ;; found the outlier
          curr
          ;; keep running
          (recur (inc offset)
                 (inc idx)))))))

(comment
  (let [inputs (get-lines "day_09/inputs.txt")]
    (slide inputs)))
