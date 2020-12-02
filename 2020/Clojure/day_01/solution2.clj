(ns solution2
  (:require [clojure.string :as str]))

(defn two-sum
  [inputs target]
  (loop [l  inputs
         seen #{}]
    (when-let [curr (first l)]
      (if-let [match (seen (- target curr))]
        (* curr match)
        (recur (rest l) (conj seen curr))))))

(defn three-sum
  [inputs target]
  (letfn [(search [x]
            (when-let [yz (two-sum inputs (- target x))]
              (* x yz)))]
    (some search inputs)))

(defn get-lines 
  "Read in inputs as seq of integers."
  [file]
  (map read-string (str/split-lines (slurp file))))

(comment
  (let [inputs [1721 979 366 299 675 1456]
        target 2020]
    (three-sum inputs target))
  
  (let [inputs (get-lines "day_01/inputs.txt")
        target 2020]
    (three-sum inputs target)))
