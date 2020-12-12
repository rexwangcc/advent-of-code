(ns day_01.solution1
  (:require [clojure.string :as str]))

(defn two-sum
  [inputs target]
  (loop [l  inputs
         seen #{}]
    (let [curr (first l)]
      (if-let [match (seen (- target curr))]
        (* curr match)
        (recur (rest l) (conj seen curr))))))

(defn get-lines
  "Read in inputs as seq of integers."
  [file]
  (map read-string (str/split-lines (slurp file))))

(comment
  (let [inputs [1721 979 366 299 675 1456]
        target 2020]
    (two-sum inputs target))

  (let [inputs (get-lines "day_01/inputs.txt")
        target 2020]
    (two-sum inputs target)))
